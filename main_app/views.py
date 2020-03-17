from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
  
def about(request):
  return render(request, 'about.html')

def rocks_index(request):
  return render(request, 'rocks/index.html', { 'rocks': rocks })

class Rock:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, color, description):
    self.name = name
    self.color = color
    self.description = description

rocks = [
  Rock('Marble', 'white', 'smooth'),
  Rock('Sandstone', 'tan', 'coarse'),
  Rock('Limestone', 'grey', 'mineral rich')
]