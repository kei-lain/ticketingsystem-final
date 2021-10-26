from django.shortcuts import render
from django.views import View
from django.http import HttpResponse ,HttpResponseForbidden ,HttpRequest
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .decorators import allowed_users
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from rest_framework import viewsets
from .serializers import TicketSerializer 

from django.urls import  reverse_lazy
import random
from .models import Ticket, Person
# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

class ticketView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'tickets'
    
    def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['tickets'] = context['tickets'].filter(user=self.request.user)
	    return context

class ticketDetail(LoginRequiredMixin, DetailView):
    model  = Ticket
    context_object_name = 'ticket'


class ticketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('tickets')


    
    

class ticketUpdate(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('tickets')


class ticketDelete(LoginRequiredMixin, DeleteView):
	model = Ticket
	context_object_name ='ticket'
	success_url = reverse_lazy('tickets')




class employeeDashboard(PermissionRequiredMixin,ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets/employee_dashboard.html'
    permission_required = 'is_staff'

    # def dispatch(self, request, *args, **kwargs):
    #         if not request.user.is_staff:
    #             logout(request)
    #             return self.handle_no_permission()
    #         return super(LogoutIfNotStaffMixin,self).dispatch( *args, **kwargs)
    
    def get_queryset(self):
        employeeDashboard().queryset = super().get_queryset().all()
        return(super().get_queryset()).all()
    
    
    def get_context_data(self, **kwargs):
        items = Ticket.objects.all()
        context_object_name = 'tickets'
        random_item = random.choice(items)
        context = super().get_context_data(**kwargs)
        context['tickets'] = context['tickets']
        if random_item:
            context['random_item'] = random_item
        return(context)
        
    
class archivedTickets(PermissionRequiredMixin,ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets/ticket_archive.html'
    permission_required = 'is_staff'
    

    # def dispatch(self, request, *args, **kwargs):
    #         if not request.user.is_staff:
    #             logout(request)
    #             return self.handle_no_permission()
    #         return super(logout(request), self).dispatch(request,    *args, **kwargs)

    def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['tickets'] = context['tickets'].filter(complete=True)
	    return context


    
    
    

    