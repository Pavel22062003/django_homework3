from django.contrib import admin

from .models import Product, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_for_buy', 'category')
    list_filter = ['category']
    search_fields = ['name', 'description']