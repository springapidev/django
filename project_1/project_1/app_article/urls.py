from django.urls import path

from app_article.views import article_view

urlpatterns = [
    path('<int:article_id>', article_view, name="article_view")
]
