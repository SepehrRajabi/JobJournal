# JobJournal

Keep track of your interviews, job applications and statuses.

A Django REST Framework API for tracking job applications, interview stages, clients, and related documents (CVs, cover letters).

## Stack

- Django + Django REST Framework
- S3-compatible object storage (RustFS) for documents, via django-storages
- `uv` for dependency management

## Getting started

```bash
uv sync
python manage.py migrate
python manage.py runserver
```

Envs managed by [envvault](https://github.com/SepehrRajabi/envvault).
