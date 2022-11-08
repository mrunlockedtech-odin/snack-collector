from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Snack:
  def __init__(self, name, type, description):
    self.name = name
    self.type = type
    self.description = description

snacks = [
  Snack('Doritos', 'Chips', 'Dust is really tasty, nice crisp'),
  Snack('Takis', 'Chips', 'Really hot for some people, blue bag'),
  Snack('Chips A-hoy', 'Cookies', 'Also come in a blue package (The main flavor)'),
]

def snacks_index(request):
  return render(request, 'snacks/index.html', {'snacks': snacks})

def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request,'about.html')