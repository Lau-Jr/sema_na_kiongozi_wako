from rest_framework import serializers
from mpis_backend import models


class MaoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maoni
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'password2']
        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'style': {"input_type": "password"}
        # }

    def save(self):
        user = models.User(username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class MikoaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['mkoa']
        model = models.Jimbo


class SektaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['jina', 'id']
        model = models.Sekta


class JimboSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jimbo
        fields = ['jina_la_jimbo', 'id']


class MikoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jimbo
        fields = ['mkoa', 'id']
