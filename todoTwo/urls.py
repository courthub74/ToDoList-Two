from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo, name='todo'),
	path('edit/', views.edit, name='edit'),
]