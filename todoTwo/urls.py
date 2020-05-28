from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo, name='todo'),
	path('projects/', views.projects, name='projects'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('cross_off/<list_id>', views.cross_off, name='cross_off'),
	path('uncross/<list_id>', views.uncross, name='uncross'),
	path('editinfo/<list_id>', views.editinfo, name='editinfo')
]