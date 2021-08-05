from django.urls import path
from . import views

urlpatterns = [
	path('', views.name, name="api"),
	path('simple/', views.simple.as_view(), name="simple"),
	
]
