from __future__ import absolute_import
from twilio.rest import Client

import arrow
import dramatiq

from django.conf import settings

from .models import Reminder

# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

@dramatiq.actor
def send_sms_reminder(reminder_id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our appointment from the database
    try:
        appointment = Reminder.objects.get(pk=reminder_id)
    except Reminder.DoesNotExist:
        # The appointment we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = 'Hi {0}. Have a great trip!'.format(
        reminder.name
    )

    client.messages.create(
        body=body,
        to=reminder.phone_number,
        from_=settings.TWILIO_NUMBER,
    )