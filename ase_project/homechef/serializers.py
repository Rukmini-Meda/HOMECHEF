from rest_framework import serializers
from .models import Vendor
from .models import FoodItem
from .models  import Ingredients

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'
        
class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodItem
        fields='__all__'

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredients
        fields='__all__'



