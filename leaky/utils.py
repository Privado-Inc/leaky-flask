import logging
import sqlite3

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

DB_PATH = "users.db"
client = WebClient(token="WOLOLO")

def query_db(query, args=(), one=False, commit=False):
    with sqlite3.connect(DB_PATH) as conn:
        conn.set_trace_callback(print)
        cur = conn.cursor().execute(query, args)
        if commit:
            conn.commit()
        return cur.fetchone() if one else cur.fetchall()

def send_slack_message(chan, msg):
    try:
        response = client.chat_postMessage(channel=chan, text=msg)
        assert response["message"]["text"] == msg
    except SlackApiError as e:
        logging.error("Slack Error: " + {e.response['error']})
        logging.error("Could not send message: " + msg)

def send_mail(content, first_name):
    message = Mail(
        from_email= first_name + '@example.com',
        to_emails='to@example.com',
        subject='You have got mail!',
        html_content="""
            Important news about <strong>%s</strong> <br> %s
            """ 
            % (first_name, content)
    )

    sg = SendGridAPIClient("SENGRID_KEY_WOLOLO")
    response = sg.send(message)
    logging.info(response.status_code)
