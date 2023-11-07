
from django.db import models

class MyMenu(models.Model):
    main_menu = models.CharField(max_length=100)  # Главное меню. Позволяет иметь несколько независимых меню, каждое с собственными пунктами.
    name = models.CharField(max_length=100)                                                       # Название пункта меню
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) # Родительский элемент меню, т.к. null=True, то он имеет родителя
    url = models.CharField(max_length=100, blank=True)      # Это для навигации при клике на пункт меню. URL может быть пустым (blank=True), что позволяет использовать именованный URL
    name_url = models.CharField(max_length=100, blank=True)                                # Именованный URL пункта меню

    def __str__(self):
        return self.name