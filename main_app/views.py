from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Snack
from .forms import PurchaseForm
# Create your views here.

class SnackCreate(CreateView):
  model = Snack
  fields= '__all__'

class SnackUpdate(UpdateView):
  model = Snack
  fields = ['type','description']

class SnackDelete(DeleteView):
  model = Snack
  success_url: '/snacks/'

def snacks_index(request):
  snacks = Snack.objects.all()
  return render(request, 'snacks/index.html', {'snacks': snacks})

def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request,'about.html')

def snacks_detail(request, snack_id):
  snack = Snack.objects.get(id=snack_id)
  purchase_form = PurchaseForm()
  return render(request, 'snacks/detail.html', { 'snack':snack, 'purchase_form':purchase_form })