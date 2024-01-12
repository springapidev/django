from django.shortcuts import render


# Create your views here.
def view_index(request):
    return render(request, 'index.html')


def view_about(request):
    return render(request, 'about.html')


def view_team(request):
    return render(request, 'team.html')
