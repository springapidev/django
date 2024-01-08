from django.http import HttpResponse


# Create your views here.
def one_view(request):
    return HttpResponse("Hello from app one")
