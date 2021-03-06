from django.db import models

# Todo Database create a Class

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item
	

class Project(models.Model):
	itemproj = models.CharField(max_length=200)
	completedproj = models.BooleanField(default=False)

	def __str__(self):
		return self.itemproj


class Deliverables(models.Model):
	delivs = models.CharField(max_length=200)
	completeddelivs = models.BooleanField(default=False)

	def __str__(self):
		return self.delivs
