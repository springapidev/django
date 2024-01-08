from django.urls import path

from app_two.views import two_view

urlpatterns =[
    path('add',two_view,name="two_view")
]