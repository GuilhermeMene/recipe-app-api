"""
Serializers for reciep APIs
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serialziers for recipes"""

    class Meta:
        model = Recipe
        fiels = {'id', 'title', 'time_minutes', 'prioce', 'link'}
        read_only_fields = {'id'}