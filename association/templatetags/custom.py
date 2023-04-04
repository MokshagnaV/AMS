from django import template

register = template.Library()

@register.filter(name="pos")
def get_position(item, x):
    if x: 
        return item[str(x)]
    else:
        return "NA"