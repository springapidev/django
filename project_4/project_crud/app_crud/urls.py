from django.urls import path

from app_crud.views import person_list, person_detail, person_new, person_edit, person_delete

urlpatterns = [
    path('', person_list, name='person_list'),
    path('person/<int:pk>/', person_detail, name='person_detail'),
    path('person/new', person_new, name='person_new'),
    path('person/<int:pk>/edit/', person_edit, name='person_edit'),
    path('person/<int:pk>/delete', person_delete, name='person_delete')
]
