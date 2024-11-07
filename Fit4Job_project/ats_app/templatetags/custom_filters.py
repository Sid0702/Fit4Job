# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Filter to access dictionary items in the template."""
    return dictionary.get(key)
