
from django import template
from Menu.models import MyMenu

register = template.Library()

@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MyMenu.objects.filter(main_menu=menu_name)
    return {'menu_items': menu_items, 'current_url': current_url}