from django.shortcuts import render
from django.http import HttpResponse
from .models import Rock


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
  
def about(request):
  return render(request, 'about.html')

def rocks_index(request):
  rocks = Rock.objects.all()  
  return render(request, 'rocks/index.html', { 'rocks': rocks })

def rocks_detail(request, cat_id):
  rock = Rock.objects.get(id=rock_id)
  return render(request, 'rocks/detail.html', { 'rock': rock })