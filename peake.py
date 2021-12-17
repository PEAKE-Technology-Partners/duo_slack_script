#!/usr/bin/env python

# Importing necessary packages
from __future__ import absolute_import
from __future__ import print_function
import duo_client
import json
import sys
import requests

# Sets our Slack message to nothing by default
message = ''


# Sends out a new message with Client Name and Status through a Web Hook
def slack_message():
    if __name__ == '__main__':
        url = "Slack Hook URL Goes Here!"
        title = 'Duo Bypass Message'
        slack_data = {
            "username": "Duo Bot",
            "icon_emoji": ":key:",
            "attachments": [
                {
                    "color": "#007500",
                    "fields": [
                        {
                            "title": title,
                            "value": message,
                            "short": "false",
                        }
                    ]
                }
            ]
        }
    else:
        exit(404)
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


# Configuration for Duo API
admin_api = duo_client.Admin(
    ikey='Duo Token Here!',
    skey='Duo Token Here!',
    host='API Endpoint Here!',
)

# Retrieve user info and name from API:
users = admin_api.get_users()
settings = admin_api.get_settings()

# Goes through all users calls slack_message when peakeadmin is in bypass.
for user in users:
    if 'bypass' in user['status'] and 'peakeadmin' in user['username']:
        message = (user['username'] + " in " + settings['name'] + " is in " + user['status'])
        slack_message()
