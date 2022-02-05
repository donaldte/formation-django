from django import template 
from django.template.defaultfilters import stringfilter

register = template.Library()

"""
{{data|filtre}}
"""
@register.filter(name="addcent")
def addcent(value):
    return value + 1000000

@register.filter(name='couper')
def couper(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, 'oooo')   

@register.filter(name="miniscule")    
@stringfilter
def miniscule(value):
    return value.upper()    