from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Snack, Dish
from .forms import PurchaseForm
# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

class SnackCreate(LoginRequiredMixin,CreateView):
  model = Snack
  fields= ['name','type','description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SnackUpdate(LoginRequiredMixin,UpdateView):
  model = Snack
  fields = ['type','description']

class SnackDelete(LoginRequiredMixin,DeleteView):
  model = Snack
  success_url = '/snacks/'

@login_required
def snacks_index(request):
  snacks = Snack.objects.filter(user=request.user)
  return render(request, 'snacks/index.html', {'snacks': snacks})

def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request,'about.html')

@login_required
def snacks_detail(request, snack_id):
  snack = Snack.objects.get(id=snack_id)
  dishes_snack_doesnt_have = Dish.objects.exclude(id__in = snack.dishes.all().values_list('id'))
  purchase_form = PurchaseForm()
  return render(request, 'snacks/detail.html', { 'snack':snack, 'purchase_form':purchase_form, 'dishes':dishes_snack_doesnt_have })

@login_required
def add_purchase(request, snack_id):
  form = PurchaseForm(request.POST)
  if form.is_valid():
    new_purchase = form.save(commit=False)
    new_purchase.snack_id = snack_id
    new_purchase.save()
  return redirect('snacks_detail', snack_id=snack_id)

class DishCreate(LoginRequiredMixin,CreateView):
  model = Dish
  fields = '__all__'

class DishList(LoginRequiredMixin,ListView):
  model = Dish

class DishDetail(LoginRequiredMixin,DetailView):
  model = Dish

class DishUpdate(LoginRequiredMixin,UpdateView):
  model = Dish
  fields = ['url']

class DishDelete(LoginRequiredMixin,DeleteView):
  model = Dish
  success_url = '/dishes/'

@login_required
def assoc_dish(request, snack_id, dish_id):
  Snack.objects.get(id=snack_id).dishes.add(dish_id)
  return redirect('snacks_detail', snack_id=snack_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('snacks_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form':form, 'error_message': error_message}
  return render(request, 'signup.html', context)