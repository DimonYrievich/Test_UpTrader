
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('menu/', include('Menu.urls')),                                  # Подключение URL-маршрутов из приложения Menu
    ]
