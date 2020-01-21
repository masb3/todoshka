from django import template
from django.utils.timezone import utc
from datetime import datetime


register = template.Library()


@register.simple_tag
def time_diff(start_date):
    return (datetime.utcnow().replace(tzinfo=utc) - start_date).days
