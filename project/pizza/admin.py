from django.contrib import admin
from .models import Pizza, Size, Ingredient


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'size', 'price', 'available']
    list_display_links = ['name']
    list_editable = ['price']
    list_filter = ['size', 'price']
    search_fields = ['^name']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['name']
    list_editable = ['price']
    list_filter = ['price']


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Size)
admin.site.register(Ingredient, IngredientAdmin)
