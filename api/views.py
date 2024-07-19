# api/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
import requests

class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def fetch_all_recipes(self):
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s='
        response = requests.get(url)
        data = response.json().get('meals', [])
        return data

    def get_queryset(self):
        recipes = self.fetch_all_recipes()
        return recipes

class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def fetch_recipe_details(self, recipe_id):
        url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}'
        response = requests.get(url)
        data = response.json().get('meals', [])[0]
        return data

    def retrieve(self, request, *args, **kwargs):
        recipe_id = self.kwargs.get('pk')
        recipe_data = self.fetch_recipe_details(recipe_id)
        serializer = self.get_serializer(recipe_data)
        return Response(serializer.data)
