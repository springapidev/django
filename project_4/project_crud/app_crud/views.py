from django.shortcuts import render, get_object_or_404, redirect

from app_crud.forms import PersonForm
from app_crud.models import Person


# Create your views here.
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'people': persons})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'person_detail.html', {'person': person})


def person_new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'person_edit.html', {'form': form})


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'person_edit.html', {'form': form})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('person_list')
