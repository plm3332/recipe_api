from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    amount = models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.name} {self.amount}'

class Recipe(models.Model):
    name = models.CharField(max_length=120, unique=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='Recipes')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name