from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.views.generic.list import ListView

from .forms import AnimalForm
from .models import Animal, Family


def create_family(request):
    if request.method == 'POST':
        family = request.POST.get('name')
        Family.objects.create(name=family)
        return redirect('home')


def update_animal(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        name = request.POST.get('name')
        family = request.POST.get('family')
        healthy = request.POST.get('healthy')
        legs = request.POST.get('legs')
        if healthy == 'Да':
            healthy = True
        else:
            healthy = False
        animal = get_object_or_404(Animal, pk=pk)
        animal.name = name
        animal.healthy = healthy
        animal.family = Family.objects.get(name=family)
        animal.legs = legs
        animal.save()
        return redirect('home')


def delete_animal(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        animal = Animal.objects.get(pk=pk)
        animal.delete()
        return redirect('home')


class AnimalsView(CreateView, ListView):
    model = Animal
    form_class = AnimalForm
    template_name = 'index.html'
    success_url = 'home'

    def get(self, request, *args, **kwargs):
        animals = Animal.objects.all()
        families = Family.objects.all()
        answer = ('Да', 'Нет')
        return render(request, self.template_name,
                      {"animals": animals, 'families': families, 'answer': answer})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        family = request.POST.get('family')
        healthy = request.POST.get('healthy')
        legs = request.POST.get('legs')
        if healthy == 'Да':
            healthy = True
        else:
            healthy = False
        animal = Animal(name=name, family=Family.objects.get(name=family), healthy=healthy, legs=legs)
        animal.save()
        return HttpResponse('ok')
