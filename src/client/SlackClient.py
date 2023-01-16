import os
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

slack_client = SlackClient(SLACK_TOKEN)


def send_message(message):
    channel_id = "my_channel_id"
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='privadobot',
        icon_emoji=':robot_face:'
    )
