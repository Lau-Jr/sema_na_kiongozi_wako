from django.urls import path
from mpis_backend.api import views

urlpatterns = [
    path('create/', views.CreateMaoniAPIView.as_view(), name='create-maoni'),
    path('rc-create/', views.CreateRegionCommissioner.as_view(), name='rc-create'),
    path('sekta/', views.SektaListAPIView.as_view(), name='sekta-list'),
    path('majimbo/<mkoa>/', views.JimboListAPIView.as_view(), name='majimbo-list'),
    path('provincies/<mkoa>/', views.MajimboListAPIView.as_view(), name='majimbo-list'),
    path('regions/', views.get_regions, name='region-list'),
    path('sectors/', views.get_sectors, name='sector-list'),
    path('check-mkoa/<mkoa>/', views.CheckMkoaAPIView.as_view(), name='check-mkoa'),
    path('getfeedback/<uname>/', views.get_feedback, name='get-feedback'),
    path('check-sekta/<jina>/', views.CheckSektaAPIView.as_view(), name='check-sekta'),
    path('check-jimbo/<mkoa>/<jimbo>/',
         views.CheckJimboAPIView.as_view(), name='check-mkoa'),
]
