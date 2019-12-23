from django.contrib import admin
from .models import Brand, Product, Category, Specifications


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'date_created', 'last_modified')


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'last_modified')


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'date_created', 'last_modified')


admin.site.register(Product, ProductAdmin)


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'unit', 'date_created', 'last_modified')


admin.site.register(Specifications, SpecificationsAdmin)
