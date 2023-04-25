from django import template
from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/base_menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name, parent__isnull=True)
    return {'menu_items': menu_items}
