from django.shortcuts import render, redirect
from .models import List, Project
from .forms import ListForm, ProjectForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

#TODOLIST
def todo(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if form.is_valid(): #if information on form is valid
			form.save()     #save the info
			all_items = List.objects.all
			messages.success(request, ('Item Has Been Added To List'))
			return render(request, 'todo.html', {'all_items': all_items})
			
	if request.method == 'POST':
		pform = ProjectForm(request.POST or None) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if pform.is_valid(): #if information on form is valid
			pform.save()     #save the info
			all_proj = Project.objects.all
			messages.success(request, ('Project Has Been Added To List'))
			return render(request, 'projects.html', {'all_proj': all_proj})


	else:
		all_items = List.objects.all
		return render(request, 'todo.html', {'all_items': all_items})


#DELETE
def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect ('todo')

#CROSS OFF
def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect ('todo')

#UNCROSS
def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect ('todo')

#EDIT
def editinfo(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)

		form = ListForm(request.POST or None, instance=item) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if form.is_valid(): #if information on form is valid
			form.save()     #save the info
			messages.success(request, ('Language Has Been Edited'))
			return redirect('todo')

	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'editinfo.html', {'item': item})



################################################################


#PROJECTS PAGE
def projects(request):
	if request.method == 'POST':
		pform = ProjectForm(request.POST or None) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if pform.is_valid(): #if information on form is valid
			pform.save()     #save the info
			all_proj = Project.objects.all
			messages.success(request, ('Project Has Been Added To List'))
			return render(request, 'projects.html', {'all_proj': all_proj})

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid(): #if information on form is valid
			form.save()     #save the info
			all_items = List.objects.all
			messages.success(request, ('Item Has Been Added To List'))
			return render(request, 'todo.html', {'all_items': all_items})
	else:
		all_proj = Project.objects.all
		return render(request, 'projects.html', {'all_proj': all_proj})

#DELETE PROJECTS
def deleteproj(request, list_id):
	pitem = Project.objects.get(pk=list_id)
	pitem.delete()
	messages.success(request, ('Project Has Been Deleted'))
	return redirect ('projects')

#CROSS OFF PROJECTS
def cross_off_project(request, list_id):
	pitem = Project.objects.get(pk=list_id)
	pitem.completedproj = True
	pitem.save()
	return redirect ('projects')

#UNCROSS PROJECTS
def uncross_project(request, list_id):
	pitem = Project.objects.get(pk=list_id)
	pitem.completedproj = False
	pitem.save()
	return redirect ('projects')

#EDIT PROJECTS
def projedit(request, list_id):
	if request.method == 'POST':
		pitem = Project.objects.get(pk=list_id)

		pform = ProjectForm(request.POST or None, instance=pitem)

		if pform.is_valid():
			pform.save()
			messages.success(request, ('Project Has Been Edited'))
			return redirect ('projects')
	else:
		pitem = Project.objects.get(pk=list_id)
		return render(request, 'projedit.html', {'pitem': pitem}) 


##################################################################

