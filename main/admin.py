from django.contrib import admin, admindocs
from django.utils.safestring import mark_safe

from .models import Category, News, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fileds= ['name']


    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100"') 
        else: 
            return "Is not image"
        


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['name', 'created_at']
    search_fileds= ['name']



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    list_filter = ['title' ,'description', 'created_at']
    search_fileds = ['title']