from django import template
import datetime
import pytz
# from gunicorn.config import User
from django.contrib.auth.models import User

register = template.Library()

location_sofia = pytz.timezone('Europe/Sofia')
current_time = datetime.datetime.now(location_sofia)
current_hour = current_time.hour


@register.simple_tag
def bg_day_or_night(request):
    return 'day' if 22 > current_hour > 6 else 'night'


@register.simple_tag
def welcome_message(request):
    if 6 < current_hour < 12:
        msg = 'Good morning. Glad to see you again!'
    elif 12 <= current_hour < 18:
        msg = 'Good afternoon. Glad to see you again!'
    elif 18 <= current_hour < 22:
        msg = 'Good evening. Glad to see you again!'
    else:
        msg = "Sleeping Mode"
    return msg
