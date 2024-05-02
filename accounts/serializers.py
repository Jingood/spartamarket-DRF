from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birth', 'gender', 'intro']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'nickname', 'birth', 'gender', 'intro']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.birth = validated_data.get('birth', instance.birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.intro = validated_data.get('intro', instance.intro)
        instance.save()
        return instance