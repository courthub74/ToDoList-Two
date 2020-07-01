from django.contrib import admin
from .models import List, Project, Deliverables 

# Register your models here.
admin.site.register(List)
admin.site.register(Project)
admin.site.register(Deliverables)