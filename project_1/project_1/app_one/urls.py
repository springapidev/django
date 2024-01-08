from django.urls import path

from app_one.views import one_view

urlpatterns = [
    path('', one_view, name="one_view")
]
