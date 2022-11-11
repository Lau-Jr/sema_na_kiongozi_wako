from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Maoni(models.Model):
    categories = [
        ('1', "1"),
        ('2', "2"),
        ('3', "3")
    ]

    phone_number = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    category = models.CharField(
        choices=categories, max_length=20, default='empty')
    jimbo = models.ForeignKey('Jimbo', related_name='maoni',
                              on_delete=models.CASCADE)
    sekta = models.ForeignKey(
        'Sekta', related_name='maoni', on_delete=models.CASCADE)
    maoni = models.CharField(max_length=255)

    def __str__(self):
        return self.maoni

    class Meta:
        verbose_name_plural = 'maoni'


class Sekta(models.Model):
    jina = models.CharField(max_length=30)

    def __str__(self):
        return self.jina


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Jimbo(models.Model):
    jina_la_jimbo = models.CharField(max_length=255)
    mkoa = models.CharField(max_length=255)
    halmashauri = models.CharField(max_length=255)
    kata = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Majimbo'

    def __str__(self):
        return self.jina_la_jimbo


class Mbunge(models.Model):
    user = models.OneToOneField(
        "User", verbose_name=("user"), on_delete=models.CASCADE)
    jimbo = models.OneToOneField(
        'Jimbo', related_name='mbunge', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'RC wa {self.jimbo}'
