                                    # Регистрация модели для отображения в админке
from django.contrib import admin
from .models import MyMenu

admin.site.register(MyMenu)