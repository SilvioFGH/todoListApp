from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view()),
    path('logout_user', views.logout_user),
    path('', views.TaskList.as_view()),
    path('task/<int:pk>/', views.TaskDetail.as_view()),
    path('task-create/', views.TaskCreate.as_view()),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view()),
    path('task-delete/<int:pk>/', views.DeleteView.as_view()),
]

