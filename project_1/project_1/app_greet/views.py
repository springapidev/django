from django.http import HttpResponse


# Create your views here.
def greet_view(request, username):
    return HttpResponse(f"Hello, {username} !")
