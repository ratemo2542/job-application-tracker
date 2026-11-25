# Job Application Tracker

A small job application tracker with a SQLite command-line interface and a browser dashboard. The CLI stores records in `jobs.db`; the browser dashboard stores its own records in this browser's localStorage.

## CLI requirements
- Python 3.10+
- No third-party packages

## CLI usage
```bash
python main.py add --company "Acme" --role "Junior Developer" --status applied
python main.py list
python main.py update 1 --status interview
python main.py stats
```

Supported statuses: `saved`, `applied`, `interview`, `offer`, `rejected`. Check `python main.py --help` for exact options.

## Browser dashboard
Open `index.html` in a browser. It is a separate local-only interface; it does not sync with the SQLite CLI or across devices.

## Security and scope
This is a local personal tracker, not a hosted multi-user service. Do not store sensitive personal data in a shared browser profile. No authentication, server-side backup, or cross-device sync is provided.
