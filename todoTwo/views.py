from django.shortcuts import render
from .models import List, Project
from .forms import ListForm, ProjectForm

# Create your views here.

#TODOLIST
def todo(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if form.is_valid(): #if information on form is valid
			form.save()     #save the info
			all_items = List.objects.all
			return render(request, 'todo.html', {'all_items': all_items})
			
	else:
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