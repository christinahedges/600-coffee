# -*- coding: utf-8 -*-

__all__ = ["send_message"]

import requests


def send_message(config, emails, message, subject=None):
    if subject is None:
        subject = config.get("email_subject", "Coffee Roulette")
    if config["debug"]:
        emails = ["christinalouisehedges@gmail.com"]
        subject = "[TEST] " + subject
    url = "https://api.mailjet.com/v3/send"
    auth = (config["mailjet_public_key"], config["mailjet_private_key"])
    data = {
        "from": config["sender_email"],
        "to": emails,
        "subject": subject,
        "text": message,
    }
    return requests.post(url, auth=auth, data=data)
