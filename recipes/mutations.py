from typing import List
import strawberry
from strawberry import auto
from strawberry.types import Info
from .models import Ingredient, Recipe
from .types import IngredientType, RecipeType

@strawberry.django.input(Ingredient)
class IngredientInput:
    name: auto
    description: auto

@strawberry.django.input(Recipe)
class RecipeInput:
    name: auto
    description: auto
    ingredients: List[int]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_ingredient(self, info: Info, input: IngredientInput) -> IngredientType:
        ingredient = Ingredient.objects.create(**input.__dict__)
        return ingredient

    @strawberry.mutation
    def update_ingredient(self, info: Info, id: int, input: IngredientInput) -> IngredientType:
        ingredient = Ingredient.objects.get(pk=id)
        for field, value in input.__dict__.items():
            setattr(ingredient, field, value)
        ingredient.save()
        return ingredient

    @strawberry.mutation
    def delete_ingredient(self, info: Info, id: int) -> bool:
        Ingredient.objects.filter(pk=id).delete()
        return True

    @strawberry.mutation
    def create_recipe(self, info: Info, input: RecipeInput) -> RecipeType:
        recipe = Recipe.objects.create(
            name=input.name,
            description=input.description,
            created_by=info.context["request"].user,
        )
        recipe.ingredients.set(input.ingredients)
        return recipe

    @strawberry.mutation
    def add_ingredient_to_recipe(self, info: Info, recipe_id: int, ingredient_id: int) -> RecipeType:
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        recipe.ingredients.add(ingredient)
        return recipe

    @strawberry.mutation
    def remove_ingredient_from_recipe(self, info: Info, recipe_id: int, ingredient_id: int) -> RecipeType:
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        recipe.ingredients.remove(ingredient)
        return recipe
