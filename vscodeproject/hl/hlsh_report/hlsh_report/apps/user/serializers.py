from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import authenticate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")
#    newpassword = serializers.CharField(
#        style={"input_type": "password"}, write_only=True, label="update password")

    class Meta:
        model = User
        # fields = [
        #     "username",
        #     "email",
        #     "password",
        #     "password2",
        # ]
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        # if (email and User.objects.filter(email=email).exclude(username=username).exists()):
        #     raise serializers.ValidationError(
        #         {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # username = validated_data["username"]
        newpassword = validated_data["newpassword"]
        # password = validated_data["password"]
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        # if (password and User.objects.filter(password=password).exclude(username=username).exists()):
        #     raise serializers.ValidationError(
        #         {"email": "Email addresses must be unique."})
        # user = authenticate(username=username, password=password)
        # if user is None:
        #     raise serializers.ValidationError(
        #         {"password": "password is error."})

        if newpassword is not None:
            instance.set_password(newpassword)

        instance.save()

        return instance
