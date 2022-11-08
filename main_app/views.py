from django.shortcuts import render
from django.http import HttpResponse
from .models import Snack
# Create your views here.

def snacks_index(request):
  snacks = Snack.objects.all()
  return render(request, 'snacks/index.html', {'snacks': snacks})

def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request,'about.html')

def snacks_detail(request, snack_id):
  snack = Snack.objects.get(id=snack_id)
  return render(request, 'snacks/detail.html', { 'snack':snack })