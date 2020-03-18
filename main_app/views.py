from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rock
from .forms import QualityForm

class RockUpdate(UpdateView):
  model = Rock
  fields = ['color', 'description']

class RockDelete(DeleteView):
  model = Rock
  success_url = '/rocks/'

class RockCreate(CreateView):
  model = Rock
  fields = '__all__'
  success_url = '/rocks/'


# Create your views here.
def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')

def rocks_index(request):
  rocks = Rock.objects.all()  
  return render(request, 'rocks/index.html', { 'rocks': rocks })

def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  quality_form = QualityForm()
  return render(request, 'rocks/detail.html', {
    'rock': rock, 'quality_form': quality_form
  })

def add_quality(request, rock_id):
  form = QualityForm(request.POST)
  if form.is_valid():
    new_quality = form.save(commit=False)
    new_quality.rock_id = rock_id
    new_quality.save()
  return redirect('detail', rock_id=rock_id)