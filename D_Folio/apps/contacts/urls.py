from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('sended/', views.request, name = 'request'),
]