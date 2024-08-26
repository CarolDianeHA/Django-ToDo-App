from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('update/<int:id>/', views.update_task, name='update'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('mark_in_progress/<int:id>/', views.mark_in_progress, name='mark_in_progress'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
]