from django.shortcuts import render, redirect
from .models import List, Project, Deliverables
from .forms import ListForm, ProjectForm, DeliverablesForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

#BASICS
def basics(request):
	return render(request, 'basics.html', {})

#TODOLIST
def todo(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if form.is_valid(): #if information on form is valid
			form.save()     #save the info
			all_items = List.objects.all
			messages.success(request, ("Practice Has Been Added To 'Practices' List"))
			return render(request, 'todo.html', {'all_items': all_items})
			
	if request.method == 'POST':
		pform = ProjectForm(request.POST or None) #create variable called form call it ListForm and populate it with the request POST or if nothing requested, do nothing

		if pform.is_valid(): #if information on form is valid
			pform.save()     #save the info
			all_proj = Project.objects.all
			messages.success(request, ("Project Has Been Added To 'Projects' List"))
			return render(request, 'projects.html', {'all_proj': all_proj})


	else:
		all_items = List.objects.all
		return render(request, 'todo.html', {'all_items': all_items})


#DELETE
def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Practice Has Been Deleted!'))
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
			messages.success(request, ('Practice Has Been Edited'))
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
			messages.success(request, ("Project Has Been Added To 'Projects' List"))
			return render(request, 'projects.html', {'all_proj': all_proj})

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid(): #if information on form is valid
			form.save()     #save the info
			all_items = List.objects.all
			messages.success(request, ("Practice Has Been Added To 'Practices' List"))
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

#DELIVERABLES

def deliverables(request):
	if request.method == 'POST':
		dform = DeliverablesForm(request.POST or None)

		if dform.is_valid():
			dform.save()
			all_delivs = Deliverables.objects.all
			messages.success(request, ('Deliverable Has Been Added To "Deliverables" List'))
			return render(request, 'deliverables.html', {'all_delivs': all_delivs})

	else:
		all_delivs = Deliverables.objects.all
		return render(request, 'deliverables.html', {'all_delivs': all_delivs})


def deletedeliverable(request, list_id):
	dedeliv = Deliverables.objects.get(pk=list_id)
	dedeliv.delete()
	messages.success(request, ("Deliverable Has Been Deleted"))
	return redirect('deliverables')


	

