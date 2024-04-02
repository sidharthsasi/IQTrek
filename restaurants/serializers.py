from rest_framework import serializers
from .models import Restaurant, Cuisine

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    cuisines = CuisineSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'