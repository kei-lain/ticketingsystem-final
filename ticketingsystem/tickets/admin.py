from django.contrib import admin
from .models import Ticket, Person

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Person)