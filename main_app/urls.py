from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('snacks/', views.snacks_index, name='snacks_index'),
    path('snacks/<int:snack_id>/', views.snacks_detail, name='snacks_detail'),
]
