from django import template
import datetime
import pytz

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
        msg = 'Good morning and welcome to my exam project!'
    elif 12 <= current_hour < 18:
        msg = 'Good afternoon and welcome to my exam project!'
    elif 18 <= current_hour < 22:
        msg = 'Good evening and welcome to my exam project!'
    else:
        msg = "Night. Time to sleep."
    return msg
