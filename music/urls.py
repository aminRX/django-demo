from django.contrib import admin
from django.urls import path, include
from .views import ListMusicians, MusicianDetail

app_name="sales"

urlpatterns = [
  path('musicians/', ListMusicians.as_view()),
  path('musicians/<int:pk>/', MusicianDetail.as_view())
]