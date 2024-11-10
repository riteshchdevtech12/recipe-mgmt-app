# Recipe Management App

Welcome to the **Recipe Management App**! This app allows you to manage ingredients and recipes using GraphQL mutations and queries. Below you'll find instructions for how to perform basic operations like creating, updating, deleting ingredients, and managing recipes.

## Table of Contents

- [Getting Started](#getting-started)
- [GraphQL Mutations](#graphql-mutations)
  - [Create Ingredient](#create-ingredient)
  - [Update Ingredient](#update-ingredient)
  - [Delete Ingredient](#delete-ingredient)
  - [Create Recipe](#create-recipe)
  - [Add Ingredient to Recipe](#add-ingredient-to-recipe)
  - [Remove Ingredient from Recipe](#remove-ingredient-from-recipe)
- [GraphQL Queries](#graphql-queries)
  - [Query All Ingredients](#query-all-ingredients)
  - [Query All Recipes](#query-all-recipes)
  - [Get Single Ingredient by ID](#get-single-ingredient-by-id)
  - [Get Single Recipe by ID](#get-single-recipe-by-id)
- [Running the App Locally](#running-the-app-locally)

## Getting Started

This app is built with GraphQL and allows you to manage ingredients and recipes through mutations and queries. To get started, ensure you have the following installed:

- Python 3.8+
- Django
- GraphQL Server (Strawberry GraphQL)
- Docker

Clone the repository and set up the application by following the instructions in the "Running the App Locally" section below.

## GraphQL Mutations

### Create Ingredient

To create a new ingredient, use the `createIngredient` mutation with the required fields:

```graphql
mutation {
  createIngredient(input: { name: "Salt", description: "A basic seasoning ingredient" }) {
    id
    name
    description
  }
}
```

### Update Ingredient

To update an existing ingredient, use the `updateIngredient` mutation with the ingredient’s `id` and the fields you want to modify:

```graphql
mutation {
  updateIngredient(id: 1, input: { name: "Sea Salt", description: "Salt from the sea" }) {
    id
    name
    description
  }
}
```

### Delete Ingredient

To delete an ingredient, use the `deleteIngredient` mutation by specifying the `id` of the ingredient you wish to delete:

```graphql
mutation {
  deleteIngredient(id: 1)
}
```

### Create Recipe

To create a recipe with a list of ingredient IDs, use the `createRecipe` mutation. Make sure the ingredient IDs you provide already exist in your database:

```graphql
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
```

### Add Ingredient to Recipe

To add an ingredient to an existing recipe, use the `addIngredientToRecipe` mutation, specifying the `recipe_id` and `ingredient_id`:

```graphql
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
```

### Remove Ingredient from Recipe

To remove an ingredient from a recipe, use the `removeIngredientFromRecipe` mutation:

```graphql
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
```

## GraphQL Queries

You can also query the data to fetch ingredients and recipes.

### Query All Ingredients

To fetch a list of all ingredients:

```graphql
query {
  allIngredients {
    id
    name
    description
  }
}
```

### Query All Recipes

To fetch a list of all recipes:

```graphql
query {
  allRecipes {
    id
    name
    description
    ingredientCount  # This is a custom field created for ingredient count
    ingredients {
      id
      name
    }
  }
}
```

### Get Single Ingredient by ID

To fetch details of a specific ingredient by its ID:

```graphql
query {
  ingredient(id: 1) {
    id
    name
    description
  }
}
```

### Get Single Recipe by ID

To fetch details of a specific recipe by its ID:

```graphql
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
```

## Running the App Locally

To run the Recipe Management App locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/recipe-mgmt-app.git
cd recipe-mgmt-app
```

### 2. Set up the environment

Make sure you have **Python 3.8+** and **Docker** installed.

### 3. Run the application with Docker Compose

Ensure Docker is installed and running on your machine.

1. In the root of your project, run:
   ```bash
   docker-compose up --build
   ```

This will build and start the application along with any required services (e.g., database).

### 4. Start the Application and access the GraphQL Playground

Once the server is running, you can access the GraphQL playground at: [http://0.0.0.0/api/graphql/](http://0.0.0.0/api/graphql/)

From there, you can test the mutations and queries mentioned above.

---

That's it! You're ready to manage your ingredients and recipes using GraphQL. Happy coding!
```
