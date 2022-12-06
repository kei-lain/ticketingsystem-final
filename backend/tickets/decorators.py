from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Person

def unauthenticated_user(view_func):
    def wrapper_func(request,  *args,**kwargs):
        return view_func(request, *args, **kwargs)
    
    return wrapper_func()

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
       def wrapper_func(request,  *args,**kwargs):
           print('Working', allowed_roles)
           if Person.role in allowed_roles:
                return view_func(request, *args, **kwargs)
           else:
                return HttpResponseForbidden()
       return wrapper_func 
    return decorator