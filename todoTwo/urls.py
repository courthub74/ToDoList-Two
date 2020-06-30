from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo, name='todo'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('cross_off/<list_id>', views.cross_off, name='cross_off'),
	path('uncross/<list_id>', views.uncross, name='uncross'),
	path('editinfo/<list_id>', views.editinfo, name='editinfo'),

	path('projects/', views.projects, name='projects'),
	path('deleteproj/<list_id>', views.deleteproj, name='deleteproj'),
	path('cross_off_project/<list_id>', views.cross_off_project, name='cross_off_project'),
	path('uncross_project/<list_id>', views.uncross_project, name='uncross_project'),
	path('projedit/<list_id>', views.projedit, name='projedit'),
	path('basics/', views.basics, name='basics'),
]