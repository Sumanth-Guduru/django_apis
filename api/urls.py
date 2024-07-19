# api/urls.py
from django.urls import path
from .views import RecipeListAPIView, RecipeDetailAPIView

urlpatterns = [
    path('recipes/', RecipeListAPIView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailAPIView.as_view(), name='recipe-detail'),
]
