from django.contrib import admin

from first_n_air.models import Category, Sneakers, Buy

# Register your models here.

admin.site.register(Category)
admin.site.register(Sneakers)
admin.site.register(Buy)