import os
from flask import Flask, request
from flask.ext.mail import Mail, Message

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

mail = Mail(app)


@app.route('/receive_email', methods=['POST'])
def email_submissions():
    email = request.values.get('email', None)
    if email:
        msg = Message(
            "Thanks for the email submission!",
            sender='pbeeson@thevariable.com',
            recipients=[email])

        mail.send(msg)
    return "OK"

if __name__ == '__main__':
    app.run()
