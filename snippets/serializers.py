from rest_framework import serializers
from snippets.models import Heroes
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import User

class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = ('id','name')

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    #
    # def create(self, validated_data):
    #     return Heroes.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance



UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, request):
        user = User.objects.create(
            username=request.get('username'),
            email=request.get('email'),
        )
        user.set_password(request.get('password'))
        user.save()

        return user