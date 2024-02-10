from django.urls import path
from . import views

urlpatterns = [
    path('ManTitle/', views.ManTitle, name='ManTitle'),
]