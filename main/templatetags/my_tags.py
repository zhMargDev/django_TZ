from django import template
from main.models import MenuBar, Menu

register = template.Library()

# Для отрисовки меню
@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    menu_bar = MenuBar.objects.get(name=menu_name)
    menus = Menu.objects.filter(parent=None)
    active_menu = get_active_menu(menus)
    return {'menu_bar': menu_bar, 'menus': menus, 'active_menu': active_menu}

# Для отрисовки активного элемента
def get_active_menu(menus):
    for menu in menus:
        if menu.url == request.path:
            return menu
        else:
            children = Menu.objects.filter(parent=menu)
            active_child = get_active_menu(children)
            if active_child:
                return active_child
    return None