from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Rock, Region
from .forms import QualityForm

class RockUpdate(LoginRequiredMixin, UpdateView):
  model = Rock
  fields = ['color', 'description']

class RockDelete(LoginRequiredMixin, DeleteView):
  model = Rock
  success_url = '/rocks/'

class RockCreate(LoginRequiredMixin, CreateView):
  model = Rock
  fields = '__all__'
  success_url = '/rocks/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


# Create your views here.
def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')

@login_required
def rocks_index(request):
  rocks = Rock.objects.filter(user=request.user)  
  return render(request, 'rocks/index.html', { 'rocks': rocks })

@login_required
def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  region_rock_doesnt_have = Region.objects.exclude(id__in = rock.region.all().values_list('id'))
  quality_form = QualityForm()
  return render(request, 'rocks/detail.html', {
    'rock': rock, 'quality_form': quality_form,
    'region': region_rock_doesnt_have
  })

@login_required
def add_quality(request, rock_id):
  form = QualityForm(request.POST)
  if form.is_valid():
    new_quality = form.save(commit=False)
    new_quality.rock_id = rock_id
    new_quality.save()
  return redirect('detail', rock_id=rock_id)

@login_required
def assoc_region(request, rock_id, region_id):
  Rock.objects.get(id=rock_id).region.add(region_id)
  return redirect('detail', rock_id=rock_id)

@login_required
def unassoc_region(request, rock_id, region_id):
  Rock.objects.get(id=rock_id).region.remove(region_id)
  return redirect('detail', rock_id=rock_id)

class RegionList(LoginRequiredMixin, ListView):
  model = Region

class RegionDetail(LoginRequiredMixin, DetailView):
  model = Region

class RegionCreate(LoginRequiredMixin, CreateView):
  model = Region
  fields = '__all__'

class RegionUpdate(LoginRequiredMixin, UpdateView):
  model = Region
  fields = ['name', 'rarity']

class RegionDelete(LoginRequiredMixin, DeleteView):
  model = Region
  success_url = '/region/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)