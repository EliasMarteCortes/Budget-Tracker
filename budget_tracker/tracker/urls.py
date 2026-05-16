from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('budgets/delete/<int:pk>/', views.delete_budget, name='delete_budget'),
]