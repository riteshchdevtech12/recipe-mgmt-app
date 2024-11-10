from typing import List
import strawberry
from .types import IngredientType, RecipeType
from .models import Ingredient, Recipe

@strawberry.type
class Query:
    all_ingredients: List[IngredientType] = strawberry.django.field()
    all_recipes: List[RecipeType] = strawberry.django.field()
    
    @strawberry.field
    def ingredient(self, id: int) -> IngredientType:
        return Ingredient.objects.get(pk=id)
    
    @strawberry.field
    def recipe(self, id: int) -> RecipeType:
        return Recipe.objects.get(pk=id)