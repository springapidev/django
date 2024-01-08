from django.urls import path

from app_three.views import three_view

urlpatterns = [
    path('', three_view, name="three_view")
]
