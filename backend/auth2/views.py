from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import  reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class customLoginView(LoginView):
	template_name = 'account/login.html'
	fields: '__all__'
	redirected_authenticasted_user = True
	def get_successful_url(self):
		return reverse_lazy('tickets')
