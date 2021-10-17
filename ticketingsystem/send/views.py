from django.shortcuts import render
from django.core.mail import send_mail
from tickets.models import Ticket, Person
# Create your views here.


def index(request):
    model = Ticket
    context_object_name = 'tickets' 
    for ticket in model.objects.all():
        if ticket.complete == True:
            send_mail(f'{ticket.briefDescription} is complete!', 
            f'Hello {ticket.user}, your ticket {ticket.briefDescription} has been completed',
             'laineytubbs@protonmail.com', [f'{ticket.user.email}'])
        else:
            pass
    return(render(request, 'send/send_index.html'))