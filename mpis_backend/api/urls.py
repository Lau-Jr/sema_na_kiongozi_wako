from django.urls import path
from mpis_backend.api import views

urlpatterns = [
    path('create/', views.CreateMaoniAPIView.as_view(), name='create-maoni'),
    path('sekta/', views.SektaListAPIView.as_view(), name='sekta-list'),
    path('majimbo/<mkoa>/', views.JimboListAPIView.as_view(), name='majimbo-list'),
    path('check-mkoa/<mkoa>/', views.CheckMkoaAPIView.as_view(), name='ckeck-mkoa'),
    path('check-sekta/<jina>/', views.CheckSektaAPIView.as_view(), name='ckeck-sekta'),
    path('check-jimbo/<mkoa>/<jimbo>/',
         views.CheckJimboAPIView.as_view(), name='ckeck-mkoa'),
]
