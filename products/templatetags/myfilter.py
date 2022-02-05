from django import template 

register = template.Library()

"""
{{data|filtre}}
"""
@register.filter(name="addcent")
def addcent(value):
    return value + 1000