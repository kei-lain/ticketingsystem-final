import django_filters

from .models import Ticket

class TicketSearchFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields ='__all__'