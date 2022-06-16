from django import template

register=template.Library

def first_eight_upper(value):
    """This is my own filter"""
    result=value[:8].upper()
    return result

register.filter('f8upper',first_eight_upper)

"""We can register filter with decorator as follows"""

@register.filter(name='f8upper')
def first_eight_upper(value):
    """This is my own filter"""
    result=value[:8].upper()
    return result

