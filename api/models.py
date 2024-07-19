# api/models.py
from django.db import models

class Recipe(models.Model):
    idMeal = models.CharField(max_length=100, unique=True)
    strMeal = models.CharField(max_length=255)
    strInstructions = models.TextField()
    strMealThumb = models.URLField()
    strTags = models.CharField(max_length=255, blank=True, null=True)
    strYoutube = models.URLField(blank=True, null=True)
    # Define more fields as needed

    def __str__(self):
        return self.strMeal
