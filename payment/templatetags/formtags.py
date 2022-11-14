from django import template
from django.forms.fields import DecimalField, EmailField, CharField

register = template.Library()

@register.filter
def addclass(value):
    if 'class' not in value.field.widget.attrs:
        if type(value.field) is EmailField:
            value = value.as_widget(attrs={'class': "input"})
        elif type(value.field) is CharField:
            value = value.as_widget(attrs={'class': "input"})
        elif type(value.field) is DecimalField:
            value = value.as_widget(attrs={'class': "input"})
    return value

