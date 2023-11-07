
from django.urls import path
from . import views                                   # from .views import menu_view - можно импортировать таким образом


urlpatterns = [
    path('<str:menu_name>/', views.menu_view, name='menu_view'),
    # Сюда можно добавлять другие URL-маршруты
    ]

# Я написал URL-маршрут для отображения меню по его имени/
# name='menu_view' - это название пути