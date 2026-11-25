# Job Application Tracker

A local SQLite-backed CLI to keep job applications organized. Track company, role, application date, status, follow-up date, and notes.

## Requirements
- Python 3.10+
- No third-party packages

## Run
```bash
python main.py add --company "Acme" --role "Junior Developer" --status applied
python main.py list
python main.py update 1 --status interview
python main.py stats
```

Supported statuses: `saved`, `applied`, `interview`, `offer`, `rejected`. Data is stored in `jobs.db`.
