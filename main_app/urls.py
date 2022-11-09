from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('snacks/', views.snacks_index, name='snacks_index'),
    path('snacks/<int:snack_id>/', views.snacks_detail, name='snacks_detail'),
    path('snacks/create/', views.SnackCreate.as_view(), name='snacks_create'),
    path('snacks/<int:pk>/delete', views.SnackDelete.as_view(), name='snacks_delete'),
    path('snacks/<int:pk>/update', views.SnackUpdate.as_view(), name='snacks_update'),
    path('snacks/<int:snack_id>/add_purchase/', views.add_purchase, name='add_purchase'),
    path('snacks/<int:snack_id>/assoc_dish/<int:dish_id>/', views.assoc_dish, name='assoc_dish'),
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dishes_detail'),
    path('dishes/', views.DishList.as_view(), name='dishes_index'),
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
