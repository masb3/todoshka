import datetime
import pytz
from django import template


register = template.Library()


@register.simple_tag
def current_time(str_format):
   return datetime.datetime.now().strftime(str_format)



