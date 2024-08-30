from django.contrib import admin # type: ignore
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description', 'price', 'slug', 'category', 'is_sale', 'created_date')
    prepopulated_fields = {
        "slug": ('name',)
    }

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description', 'created_date')



admin.site.register(models.Products, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)