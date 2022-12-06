from django.contrib import admin
from django.urls import path, include
from .views import ticketView, ticketCreate , ticketDetail, ticketUpdate, ticketDelete, employeeDashboard , archivedTickets

urlpatterns = [
    path('', ticketView.as_view(), name='tickets'),
    path('tickets/<int:pk>/', ticketDetail.as_view(), name='ticket'),
    path('create-ticket/', ticketCreate.as_view(), name='ticket-create') ,
    path('update-ticket/<int:pk>/==', ticketUpdate.as_view(), name= 'update-ticket'),
    path('delete-ticket/<int:pk>/==', ticketDelete.as_view(), name= 'delete-ticket'),
    path('dashboard/', employeeDashboard.as_view(), name='employee-dashboard' ),
    # path('dashboard/search', SearchResultsView.as_view(), name='search-results'),
    path('archive/', archivedTickets.as_view(), name='ticket-archive' )
]