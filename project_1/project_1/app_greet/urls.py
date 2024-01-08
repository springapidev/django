from django.urls import path

from app_greet.views import greet_view

urlpatterns = [
    path('<str:username>/', greet_view, name="greet_view")
]
