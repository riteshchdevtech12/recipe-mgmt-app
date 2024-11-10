from django.contrib import admin
from .models import Recipe, Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", ]


class IngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    list_filter = ["created_by"]
    inlines = [IngredientInline]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
