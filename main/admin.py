from django.contrib import admin
from merch.models import Categories, Products


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

