from rest_framework import serializers
from posts.models import Posts
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = Posts
        fields = ('created', 'description', 'img')
        write_only_fields = ('password',)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Posts.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.created)
        instance.description = validated_data.get('description', instance.description)
        instance.img = validated_data.get('img', instance.img)
        instance.save()
        return instance

    class Meta:
        model = Posts
        fields = ('created','description','img')
