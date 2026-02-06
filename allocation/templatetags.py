from django import template
from datetime import time, datetime

register = template.Library()

@register.filter
def format_12hour(value):
    """
    Convert time to 12-hour format with AM/PM
    Usage: {{ time_object|format_12hour }}
    """
    if isinstance(value, time):
        return value.strftime("%I:%M %p")
    elif isinstance(value, datetime):
        return value.strftime("%I:%M %p")
    return value

@register.filter
def format_12hour_simple(value):
    """
    Convert time to 12-hour format without leading zero, with AM/PM
    Usage: {{ time_object|format_12hour_simple }}
    """
    if isinstance(value, time):
        hour = int(value.strftime("%I"))
        minute = value.strftime("%M")
        meridiem = value.strftime("%p")
        return f"{hour}:{minute} {meridiem}"
    elif isinstance(value, datetime):
        hour = int(value.strftime("%I"))
        minute = value.strftime("%M")
        meridiem = value.strftime("%p")
        return f"{hour}:{minute} {meridiem}"
    return value
