# Leaky Flask

A Flask app that leaks or shares important PII data to local as well as third party data processors

## Build and Run

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
FLASK_APP=run.py flask run
```

### Third Party Sharing
 - Sentry
 - Slack
 - Sendgrid

### Storage
 - Local DB via `sqlite`

### Leaks
 - Python `logging`

