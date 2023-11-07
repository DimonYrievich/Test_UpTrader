
from django.shortcuts import render
# MyMenu используется в файле menu_tags.py, где определен тег draw_menu.

def menu_view(request, menu_name='main_menu'):
    current_url = request.path
    return render(request, 'menu_template.html', {'menu_name': menu_name, 'current_url': current_url})