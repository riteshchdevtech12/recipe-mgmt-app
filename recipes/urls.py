from django.urls import path
from strawberry.django.views import GraphQLView
from recipes.schema import schema


urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema)),
]
