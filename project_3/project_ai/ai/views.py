from django.shortcuts import render, redirect

from ai.forms import PersonForm
from ai.models import Person


# Create your views here.
def view_index(request):
    return render(request, 'index.html')


def view_about(request):
    return render(request, 'about.html')


def view_services(request):
    return render(request, 'services.html')


def view_projects(request):
    return render(request, 'project.html')


def view_features(request):
    return render(request, 'features.html')


def view_team(request):
    return render(request, 'team.html')


def view_testimonials(request):
    return render(request, 'testimonials.html')


def view_faq(request):
    return render(request, 'faq.html')


def view_contact(request):
    return render(request, 'contact.html')


def view_404(request):
    return render(request, '404.html')


# Database Related Tasks: Person Add
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PersonForm()

    return render(request, 'person_add.html', {'form': form})


def list_person(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})
