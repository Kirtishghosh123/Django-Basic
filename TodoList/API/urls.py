
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CreateUser.as_view(), name='just-user'),
    path('users/<int:id>/', views.UserDetailOPS.as_view(), name="user-detail"),
    path('users/<int:id>/alltasks/', views.CreateTask.as_view(), name="user-tasks"),
    path('users/<int:user_id>/tasks/<int:task_id>/', views.GetDetailedTask.as_view(), name="user-detail-tasks"),
    path('users/<int:user_id>/tasks/', views.UserTasksFilter.as_view(), name="user-tasks-filter"),
]
