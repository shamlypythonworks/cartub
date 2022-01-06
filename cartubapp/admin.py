from django.contrib import admin
from .models import Category
from .models import products
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('catname',)}
admin.site.register(Category,catadmin)
class proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,proadmin)