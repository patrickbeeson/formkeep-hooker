import os
from flask import Flask, request
from flask.ext.mail import Mail, Message
from . import app

app.config.from_object(os.environ['APP_SETTINGS'])

mail = Mail(app)


@app.route('/receive_email', methods=['POST'])
def email_submissions():
    email = request.values.get('email', None)
    if email:
        msg = Message(
            "Thanks for the email submission!",
            sender='noreply@isyourwaterwater.com',
            recipients=[email])

        mail.send(msg)
    else:
        return b"OH NO"
    return b"OK"
