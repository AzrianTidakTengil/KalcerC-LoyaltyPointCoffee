from django import template

register = template.Library()

@register.filter
def rupiah(value):
    try:
        return "Rp {:,}".format(int(value)).replace(",", ".")
    except:
        return value
