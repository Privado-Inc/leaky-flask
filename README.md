# Leaky Flask

A Flask app that leaks or shares important PII data to local as well as third party data processors

## Build and Run

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

flask db init 
flask db migrate 
flask db upgrade 
flask db downgrade 

python app.py
```


### Third Party Sharing
 - Sentry
 - Slack
 - Sendgrid

### Storage
 - Local DB via `sqlite`

### Leaks
 - Python `logging`

#### Skeleton Reference
https://plainenglish.io/blog/flask-crud-application-using-mvc-architecture
