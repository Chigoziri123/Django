from django.contrib import admin
from .models import Product, Store, Category, Rating

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    list_filter = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','store','category')
    list_filter = ('category', 'store')
    list_per_page = 10

admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Rating)

