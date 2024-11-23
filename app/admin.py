from django.contrib import admin
from .models import *

# регистрируем модель на сайте администрирования
admin.site.register(User)
