from functools import wraps
from django.shortcuts import redirect
from .models import Person

def only_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            # Redirige l'administrateur vers une vue spécifique après la connexion
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view

def match(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view

def new(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser and request.user.last_login is None:
            
            return redirect('detail')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view

def genre(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.person.genre is not None:
            return redirect('update' , id=request.user.id - 1)
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view