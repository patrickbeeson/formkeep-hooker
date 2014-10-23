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
    message_type = request.values.get('message_type', None)
    if email and message_type == 'promo':
        msg = Message(
            body=textwrap.dedent("""\
            You are receiving this email because you submitted your email
            address at isyourwaterwater.com.\n
            -------------------------\n
            PRIMO TAKES THE RISK OUT OF WATER.\n
            We believe a healthy lifestyle starts with the water you drink.
            With high-quality Primo water in your home, there are no chances to
             take -- you'll enjoy glass after glass of safe, refreshing,
            healthy water.\n
            We'd like to help you become a part of the Primo family. Just enter
            the promo code FRACKNO at PrimoWater.com to get XX% off your
            purchase of an innovative Primo dispenser.\n
            http://somelink.com\n
            -------------------------\n
            isyourwaterwater.com"""),
            subject='Thank You For Your Interest in Primo Water',
            sender='noreply@isyourwaterwater.com',
            recipients=[email])
        mail.send(msg)
    elif email and message_type == 'water_issues':
        msg = Message(
            body=textwrap.dedent("""\
            You are receiving this email because you submitted your email
            address at isyourwaterwater.com.\n
            -------------------------\n
            DRINKING WATER SHOULDN\'T COME WITH RISKS.\n
            Our drinking water is our most precious commodity. Unfortunately,
            environmental issues such as fracking, chlorine, run off and more
            have the potential to pollute the water that comes out of your tap.\n
            At Primo, we believe a healthy lifestyle starts with the water you
            drink, and we want to keep you informed about the water in your
            area. Be on the lookout for future emails, and be sure to tell your
             friends about IsYourWaterWater.com.\n
            In the meantime, if you're unsure of the quality of the water in
            your area, you can substitute clean water from outside sources for
            your tap water.\n
            -------------------------\n
            isyourwaterwater.com"""),
            subject='Thank You For Your Interest In Water Issues',
            sender='noreply@isyourwaterwater.com',
            recipients=[email])
        mail.send(msg)
    else:
        return b"OH NO"
    return b"OK"
