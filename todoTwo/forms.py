from django import forms
from .models import List, Project, Deliverables

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ["item", "completed"]

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ["itemproj", "completedproj"]


class DeliverablesForm(forms.ModelForm):
	class Meta:
		model = Deliverables
		fields = ["delivs", "completeddelivs"]

