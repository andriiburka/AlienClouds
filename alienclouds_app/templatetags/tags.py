from django.contrib.auth.models import User
from django import template
import datetime
import pytz


register = template.Library()


@register.simple_tag
def bg_day_or_night(request):
    return 'day' if 22 > current_hour > 6 else 'night'


# ______________________________________________________________________________
users = [user for user in User.objects.all() if not user.is_superuser].__len__()

location_sofia = pytz.timezone('Europe/Sofia')
current_time = datetime.datetime.now(location_sofia)
current_hour = current_time.hour


@register.simple_tag
def welcome_message(request):
    if 6 < current_hour < 12:
        msg = f'Good morning!\n{users} users'
    elif 12 <= current_hour < 18:
        msg = f'Good afternoon.\n{users} users'
    elif 18 <= current_hour < 22:
        msg = f'Good evening.\n{users} users'
    else:
        msg = f'Sleep Mode.\n{users} users'
    return msg
# ______________________________________________________________________________
