from django.shortcuts import render
from .models import List, Project
from .forms import ListForm

# Create your views here.

#TODOLIST
def todo(request):
	all_items = List.objects.all
	return render(request, 'todo.html', {'all_items': all_items})

#PROJECTS
def proj(request):
	all_proj = Project.objects.all
	return render(request, 'todo.html', {'all_proj': all_proj})

#EDIT
def edit(request):
	all_proj = Project.objects.all
	return render(request, 'edit.html', {'all_proj': all_proj})