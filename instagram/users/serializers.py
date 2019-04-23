from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'description', 'img_profile')
        write_only_fields = ('password',)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.description = validated_data.get('description', instance.description)
        instance.img_profile = validated_data.get('img_profile', instance.img_profile)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'description', 'img_profile')
        write_only_fields = ('password',)