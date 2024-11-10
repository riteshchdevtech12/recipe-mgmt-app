# recipe-mgmt-app



1. Create Ingredient
To create an ingredient, use the createIngredient mutation with the necessary input fields:

mutation {
  createIngredient(input: { name: "Salt", description: "A basic seasoning ingredient" }) {
    id
    name
    description
  }
}

2. Update Ingredient
To update an ingredient, use the updateIngredient mutation with the ingredient’s id and the fields you wish to modify:

mutation {
  updateIngredient(id: 1, input: { name: "Sea Salt", description: "Salt from the sea" }) {
    id
    name
    description
  }
}

3. Delete Ingredient
To delete an ingredient, use the deleteIngredient mutation with the id of the ingredient you wish to delete. This mutation returns a boolean true on success:

mutation {
  deleteIngredient(id: 1)
}

4. Create Recipe
To create a recipe with a list of ingredient IDs, use the createRecipe mutation. Make sure the ingredient IDs you provide already exist in your database.

mutation {
  createRecipe(input: {
    name: "Spaghetti Bolognese",
    description: "A classic Italian pasta dish",
    ingredients: [1, 2]  # List ingredient IDs here
  }) {
    id
    name
    description
    ingredients {
      id
      name
    }
  }
}


5. Add Ingredient to Recipe
To add an ingredient to an existing recipe, use the addIngredientToRecipe mutation, specifying the recipe_id and ingredient_id:

mutation {
  addIngredientToRecipe(recipeId: 1, ingredientId: 2) {
    id
    name
    ingredients {
      id
      name
    }
  }
}


6. Remove Ingredient from Recipe
To remove an ingredient from a recipe, use the removeIngredientFromRecipe mutation:

mutation {
  removeIngredientFromRecipe(recipeId: 1, ingredientId: 2) {
    id
    name
    ingredients {
      id
      name
    }
  }
}


Running Queries
You can also run queries to fetch ingredients and recipes:

1. Query All Ingredients

query {
  allIngredients {
    id
    name
    description
  }
}


2. Query All Recipes

query {
  allRecipes {
    id
    name
    description
    ingredientCount  # This is the custom field created
    ingredients {
      id
      name
    }
  }
}

3. Get Single Ingredient by ID

query {
  ingredient(id: 1) {
    id
    name
    description
  }
}

4. Get Single Recipe by ID

query {
  recipe(id: 1) {
    id
    name
    description
    ingredientCount
    ingredients {
      id
      name
    }
  }
}
