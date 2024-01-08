from django.http import HttpResponse


# Create your views here.
def two_view(request):
    return HttpResponse("Hello from APP Two")
