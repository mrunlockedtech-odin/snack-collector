from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Snack, Dish
from .forms import PurchaseForm
# Create your views here.

class SnackCreate(CreateView):
  model = Snack
  fields= ['name','type','description']

class SnackUpdate(UpdateView):
  model = Snack
  fields = ['type','description']

class SnackDelete(DeleteView):
  model = Snack
  success_url = '/snacks/'

def snacks_index(request):
  snacks = Snack.objects.all()
  return render(request, 'snacks/index.html', {'snacks': snacks})

def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request,'about.html')

def snacks_detail(request, snack_id):
  snack = Snack.objects.get(id=snack_id)
  dishes_snack_doesnt_have = Dish.objects.exclude(id__in = snack.dishes.all().values_list('id'))
  purchase_form = PurchaseForm()
  return render(request, 'snacks/detail.html', { 'snack':snack, 'purchase_form':purchase_form, 'dishes':dishes_snack_doesnt_have })

def add_purchase(request, snack_id):
  form = PurchaseForm(request.POST)
  if form.is_valid():
    new_purchase = form.save(commit=False)
    new_purchase.snack_id = snack_id
    new_purchase.save()
  return redirect('snacks_detail', snack_id=snack_id)

class DishCreate(CreateView):
  model = Dish
  fields = '__all__'

class DishList(ListView):
  model = Dish

class DishDetail(DetailView):
  model = Dish

class DishUpdate(UpdateView):
  model = Dish
  fields = ['url']

class DishDelete(DeleteView):
  model = Dish
  success_url = '/dishes/'

def assoc_dish(request, snack_id, dish_id):
  Snack.objects.get(id=snack_id).dishes.add(dish_id)
  return redirect('snacks_detail', snack_id=snack_id)