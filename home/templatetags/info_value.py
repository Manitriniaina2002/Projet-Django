from django import template

register = template.Library()

@register.filter
def info_value(path):
    # FileInfo model has been removed (File Manager project cleanup)
    return ""
