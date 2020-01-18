from django import template
register = template.Library()
@register.filter(name='covertTime')
def time(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    return "%d:%d" %(minutes, seconds)

