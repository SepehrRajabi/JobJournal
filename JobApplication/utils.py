from django.db.models import F
from django.utils import timezone

from .models import JobApplication


def parse_time_window(time_window: str):
    """_summary_

    Args:
        time_window (str): dash-separated string representing the time window (e.g., "2023-01-01 - 2023-12-31").
    """

    if "-" not in time_window:
        raise ValueError(
            "Invalid time window format. Please provide a dash-separated string (e.g., '2023-01-01 - 2023-12-31')."
        )

    lower, upper = time_window.split("-")

    lower = lower.strip() if lower is not None else None
    upper = upper.strip() if upper is not None else None

    if lower:
        lower = timezone.datetime.strptime(lower, "%Y-%m-%d").date()
    if upper:
        upper = timezone.datetime.strptime(upper, "%Y-%m-%d").date()

    return lower, upper


def get_job_application_history(job_application: JobApplication) -> list:
    """
    Get the history of a job application, including changes to its fields and related tags.

    Args:
        job_application (JobApplication): The job application instance.
    Returns:
        list: A list of historical records.
    """
    history = job_application.history.all().order_by(
        F("history_date").desc(nulls_last=True)
    )
    history_data = []

    record = history.first()
    while record is not None:
        previous_record = record.prev_record

        if previous_record is not None:
            changes = {}
            for field in record.diff_against(
                previous_record, foreign_keys_are_objs=True
            ).changes:
                changes[field.field] = {
                    "old": field.old.title if hasattr(field.old, "title") else None,
                    "new": field.new.title if hasattr(field.new, "title") else None,
                }

            # tag_titles = [tag.title for tag in record.instance.tags.all()]

            history_data.append(
                {
                    "history_date": timezone.localtime(record.history_date),
                    "history_user": f"{record.history_user.first_name} {record.history_user.last_name}"
                    if record.history_user
                    else None,
                    "changes": changes,
                    # "tags": tag_titles,
                }
            )

        record = record.next_record

    return history_data
