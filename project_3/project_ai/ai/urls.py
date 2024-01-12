from django.urls import path

from ai.views import view_about, view_services

urlpatterns = [
    path('about/', view_about, name="ai"),
path('service/', view_services, name="ai")
]
