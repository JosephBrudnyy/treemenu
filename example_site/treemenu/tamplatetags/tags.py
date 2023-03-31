from django import template

register = template.Library()

@register.inclusion_tag('treemenu/menu.html')
def show_menu():
    
    return {'menu' : menu}