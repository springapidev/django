from django.shortcuts import render


# Create your views here.
def view_about(request):
    return render(request, 'about.html')


def view_services(request):
    return render(request, 'services.html')
