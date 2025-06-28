from django import template

# Register the template library
register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Custom Django template filter to retrieve a value from a dictionary by key.

    Usage in templates:
        {{ my_dict|get_item:"some_key" }}

    This is particularly useful when passing context as a dictionary and accessing
    dynamic keys in your templates (e.g., section lookup based on slugs).
    """
    return dictionary.get(key)
