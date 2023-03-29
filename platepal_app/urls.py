from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipiesList.as_view(), name='home'),
]
