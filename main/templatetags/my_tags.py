from django import template
from main.models import Menu

register = template.Library() #Для регистрации тегов

@register.inclusion_tag('main/menue_bar.html')
def menues():
    menus = [
        {
            'url': 'www',
            'title': 'test'
        }
    ]
    html_code = ""
    for menu in menus:
        html_code += f"""
                <a href="{menu['url']}">{menu['title']}</a>
            """
    return {'tag': html_code}
    #return Menu.objects.all()

