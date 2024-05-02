from rest_framework import serializers
from accounts.models import User
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ['author']
