# Leaky Flask

A Flask app that leaks or shares important PII data to local as well as third party data processors

## Build and Run

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

flask db init 
flask db migrate 
flask db upgrade 
flask db downgrade 

python app.py
```

### API endpoints
<br/>

#### GET
`Get user by Id` [http://127.0.0.1:5000/users/1]() 
<br/>

#### POST
`Create user` [http://127.0.0.1:5000/users]() 

`Request Body`:

```
{
        "firstname": "Hitesh",
	"address": "India",
	"age": 12
}
```

<br/>


### Third Party Sharing
 - Sentry
 - Slack
 - Sendgrid

### Storage
 - Local DB via `sqlite`

### Leaks
 - Python `logging`

#### Flask Skeleton Reference
https://plainenglish.io/blog/flask-crud-application-using-mvc-architecture

#### Sentry Integration Reference
https://docs.sentry.io/platforms/python/guides/flask/