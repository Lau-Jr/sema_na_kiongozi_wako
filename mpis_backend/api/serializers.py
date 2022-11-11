from rest_framework import serializers
from mpis_backend import models


class MaoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maoni
        fields = '__all__'


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
