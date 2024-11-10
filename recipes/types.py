from typing import List
import strawberry
from strawberry import auto
from .models import Ingredient, Recipe


@strawberry.django.type(Ingredient, pagination=True)
class IngredientType:
    id: auto
    name: auto
    description: auto


@strawberry.django.type(Recipe, pagination=True)
class RecipeType:
    id: auto
    name: auto
    description: auto
    ingredients: List[IngredientType]

    @strawberry.field
    def ingredient_count(self) -> int:
        return self.ingredients.count()