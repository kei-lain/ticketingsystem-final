from django.urls import path
from .views import customLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('login/', customLoginView.as_view(), name = 'login'),
	path('logout/',LogoutView.as_view(), name='logout')
]