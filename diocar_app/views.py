from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm
from django.db.models import Q

# function for listing all objects from Person
def person_list(request):
    people = Person.objects.all()
    return render(request, 'diocar_app/person_list.html', {'people': people})

# function for creating a new person (post request)
def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'diocar_app/person_edit.html', {'form': form})

# function for editing the existing person (post request)
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'diocar_app/person_edit.html', {'form': form, 'person': person})

# function for deleting person from list
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('person_list')
