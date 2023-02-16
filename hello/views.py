import re

from django.http import HttpResponse
from django.utils.timezone import datetime


def home(request):   # pyright: ignore
    return HttpResponse('Hello World')

def hello_there(request, name):     # pyright: ignore
    now = datetime.now()
    formatted_now = now.strftime('%A, %d %B, %Y at %X')

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match('[a-zA-Z]+', name)

    if match_object:
        cleaned_name = match_object.group(0)
    else:
        cleaned_name = 'Friend'

    # content = 'Hello there, {}! It is now {}'.format(cleaned_name, formatted_now)
    content = f'Hello there, {cleaned_name}! It is now {formatted_now}'
    return HttpResponse(content)
