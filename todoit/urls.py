from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('add', views.add_page, name="add"),
    path('edit/<int:id>/', views.edit_task_page, name="edit"),
    path('done/', views.task_done, name="done"),
]