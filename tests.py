import unittest
from flask import Flask
from flask.ext.mail import Mail, Message
from app import app
import os
from app.views import email_submissions


class TestCase(unittest.TestCase):

    TESTING = True
    MAIL_DEFAULT_SENDER = "noreply@test.com"

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(os.environ['APP_SETTINGS'])
        self.client = app.test_client()
        self.mail = Mail(self.app)
        self.ctx = self.app.test_request_context()
        self.ctx.push()
        self.email = "test@mail.com"

    def tearDown(self):
        self.ctx.pop()


class TestMessage(TestCase):

    def test_init(self):
        msg = Message(
            subject='subject',
            recipients=['test@test.com']
        )
        self.assertEqual(
            msg.sender,
            self.app.extensions['mail'].default_sender
        )
        self.assertEqual(msg.recipients, ['test@test.com'])

    def test_message_str(self):
        msg = Message(sender="from@example.com",
                      subject="subject",
                      recipients=["to@example.com"],
                      body="some plain text")
        self.assertEqual(msg.as_string(), str(msg))

    def test_email_submissions_returns_correctly(self):
        self.assertEqual(email_submissions(), b"OH NO")

    def test_email_submissions_with_required_data(self):
        response = self.client.post(
            '/receive_email',
            data={'email': 'test@test.com'}
        )
        self.assertEqual(response.status_code, 200)

    def test_email_submissions_without_email_address(self):
        response = self.client.post('/receive_email')
        self.assertEqual(response.get_data(), b"OH NO")

    def test_home_returns_message(self):
        response = self.client.get('/')
        self.assertEqual(
            response.get_data(),
            b"Nothing to see here. Move along."
        )

if __name__ == '__main__':
    unittest.main()
