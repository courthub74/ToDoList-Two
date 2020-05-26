from django.contrib import admin
from django.urls import path, include
from todoTwo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoTwo.urls'))
]
