from django.contrib import admin
from .models import Products, Categories


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'product_name',
        'price',
        'stock_quantity',
        'brand',
        'category',
        'created_at'
    )

    search_fields = (
        'product_name',
        'brand',
    )

    list_filter = (
        'category',
        'brand',
    )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    list_display = (
        'category_id',
        'category_name',
        'description',
    )

    search_fields = (
        'category_name',
    )