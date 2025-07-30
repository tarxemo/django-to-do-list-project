from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('toggle/<int:pk>/', views.toggle_todo_status, name='toggle_todo_status'),
    path('signup/', views.signup, name='signup'),
    path('logout_user/', views.logout, name='logout_user'),
]