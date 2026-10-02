from itertools import pairwise

from django.db.models import F
from django.utils import timezone

from .models import JobApplication


def parse_time_window(time_window: str, sep: str = "-") -> tuple[str, str]:
    """Parses time window string into lower and upper date bounds.

    Args:
        time_window (str): dash-separated string representing the time window (e.g., "2023-01-01 - 2023-12-31").
        sep (str): The separator string (default is "-").
    """

    if sep not in time_window:
        raise ValueError(
            "Invalid time window format. Please provide a dash-separated string (e.g., '2023-01-01 - 2023-12-31')."
        )

    lower, upper = time_window.split(sep)

    lower = lower.strip() if lower is not None else None
    upper = upper.strip() if upper is not None else None

    if lower:
        lower = timezone.datetime.strptime(lower, "%Y-%m-%d").date()
    if upper:
        upper = timezone.datetime.strptime(upper, "%Y-%m-%d").date()

    return lower, upper


def get_job_application_history(job_application: JobApplication) -> list:
    """
    Get the history of a job application, including changes to its fields.

    History is ordered most-recent-first. The initial creation snapshot has
    no previous record to diff against, so it's naturally excluded.

    Args:
        job_application (JobApplication): The job application instance.
    Returns:
        list: A list of historical records.
    """
    records = list(
        job_application.history.all().order_by(F("history_date").asc(nulls_last=True))
    )

    history_data = []
    for previous_record, record in pairwise(records):
        diff = record.diff_against(previous_record, foreign_keys_are_objs=True)
        changes = {
            field.field: {
                "old": None if field.old is None else str(field.old),
                "new": None if field.new is None else str(field.new),
            }
            for field in diff.changes
        }

        history_data.append(
            {
                "history_date": timezone.localtime(record.history_date),
                "history_user": f"{record.history_user.first_name} {record.history_user.last_name}"
                if record.history_user
                else None,
                "changes": changes,
            }
        )

    history_data.reverse()
    return history_data
