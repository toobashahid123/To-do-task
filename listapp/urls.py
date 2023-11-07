from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('delete_task/<int:task_id>', views.delete, name="delete_task"),
]
