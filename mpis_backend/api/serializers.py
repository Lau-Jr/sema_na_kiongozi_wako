from rest_framework import serializers
from mpis_backend import models
from django.db.utils import IntegrityError

class MaoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maoni
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'password2']

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

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


class MbugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mbunge
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    region = serializers.CharField(max_length=50)
    username = serializers.CharField(write_only=True)

    def save(self):
        regions_from_db = set(models.Jimbo.objects.values_list('mkoa', flat=True))
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        region = self.validated_data['region']
        username = self.validated_data['username']
        user = models.User(username=username)
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user.set_password(password)
        try:
            print('entering rc saving function')
            user = models.User(username=username)
            u = user.save()
            if region not in regions_from_db:
                raise serializers.ValidationError({'region': 'region not found'})
            rc = models.RC(region=region, user=user)
            rc = rc.save()
            print('exiting rc saving function')
        except IntegrityError as e:
            print('in exception block')
            print(e.args[-1])
            raise serializers.ValidationError({"username": e.args[-1]})

