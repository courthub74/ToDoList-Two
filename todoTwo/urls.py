from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo, name='todo'),
	path('edit/', views.edit, name='edit'),
	path('delete/<list_id>', views.delete, name='delete')
]