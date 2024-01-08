from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
articles = [
    {'id': 100, 'title': 'Article 1', 'author': 'Mr. A', 'content': 'This is the content of article 1'},
    {'id': 200, 'title': 'Article 2', 'author': 'Mr. A', 'content': 'This is the content of article 2'},
    {'id': 300, 'title': 'Article 3', 'author': 'Mr. A', 'content': 'This is the content of article 3'},
    {'id': 400, 'title': 'Article 4', 'author': 'Mr. A', 'content': 'This is the content of article 4'},
    {'id': 500, 'title': 'Article 5', 'author': 'Mr. A', 'content': 'This is the content of article 5'}
]


def article_view(request, article_id):
    article = next((article for article in articles if article['id'] == article_id), None)
    if article is None:
        return HttpResponse("Article ID not Found")

    return render(request, 'article.html', {'obtained_article': article})
