from django import template
import datetime

register = template.Library()

@register.filter
def subtract(value, arg):
    return float("{:.2f}".format(float(value) - float(arg)))

def only_postive_number(value):
    return abs(value)
register.filter('positive',only_postive_number)

def percent_change(arg1, arg2):
    return float("{:.2f}".format((float(arg1) - float(arg2)) / float(arg1) * 100))
register.filter('percentChange',percent_change)

def float_roundup(arg1):
    return float("{:.2f}".format(float(arg1)))
register.filter('floatRoundup',float_roundup)

@register.filter
def listIndex(arg1, position):
    return arg1[position]

@register.filter
def readableDate(arg1):
    d = datetime.datetime.strptime(arg1, '%Y-%m-%d')
    return d.strftime('%b %d, %Y')

@register.filter
def multiply(arg1, arg2):
    try:
        arg1 = float(arg1)
        return float_roundup(arg1 * arg2)
    except ValueError:
        return "None"
        
