from django.urls import path

from app_test.views import view_about, view_team, view_index

urlpatterns = [
    path('', view_index, name="app_test"),
    path('about/', view_about, name="app_test"),
    path('team/', view_team, name="app_test")
]
