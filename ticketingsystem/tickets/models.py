from django.db import models
from django.utils.decorators import method_decorator
from django.db.models.aggregates import Count
from django.contrib.auth.models import User, UserManager
from django import forms 


# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    endUser = 1
    employee = 2
    admin = 3

    ROLE_CHOICES = (
        (endUser, 'EndUser'),
        (employee, 'Employee'),
        (admin , 'Admin'),

    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        permissions = (
            ('can_see_dashboard', 'Can see all'),
        )

class Ticket (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    useraffected = models.ForeignKey(Person,default=1 ,on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, default=1)
    briefDescription = models.CharField(max_length=200)
    issueCategory = forms.CharField()
    severity = forms.IntegerField(required=True, max_value=4, min_value=1)
    siteAffected = forms.CharField()
    description = models.TextField(null=True,blank=True)
    equipmentTag = models.CharField(max_length=20,null=True,blank=True)
    troubleshooting = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)

    def get_queryset(self):
        return(super(Ticket, self).get_queryset()).all()

    def __str__(self):
        return self.briefDescription
    
    class Meta:
	    ordering= ['complete'] 









    
