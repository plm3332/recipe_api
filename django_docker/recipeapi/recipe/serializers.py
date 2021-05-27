from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Ingredient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Ingredient
        fields = ('name', 'amount')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        ordering = []
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'image')
    
    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredients')
        recipe, created = Recipe.objects.get_or_create(**validated_data)
        print("validated_data: ", validated_data)
        print("Recipe: ", recipe)
        if ingredient_data:
            for data in ingredient_data:
                print("data = ", data, flush=True)
                ingredient, created = Ingredient.objects.get_or_create(name=data['name'], amount=data['amount'])
                recipe.ingredients.add(ingredient)
        return recipe