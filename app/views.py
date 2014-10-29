import os
import textwrap
from flask import Flask, request
from flask.ext.mail import Mail, Message
from . import app

app.config.from_object(os.environ['APP_SETTINGS'])

mail = Mail(app)


@app.route('/')
def home():
    return "Nothing to see here. Move along."


@app.route('/receive_email', methods=['POST'])
def email_submissions():
    email = request.values.get('email', None)
    if email:
        msg = Message(
            body=textwrap.dedent("""\
            You are receiving this email because you submitted your email
            address at someurl.com."""),
            subject='Thank You For Your Interest!',
            sender='noreply@someurl.com',
            recipients=[email])
        mail.send(msg)
    else:
        return b"OH NO"
    return b"OK"
