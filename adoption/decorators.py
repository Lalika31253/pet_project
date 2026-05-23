from functools import wraps
from django.http import HttpResponseForbidden
from .utils import get_user_role

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if get_user_role(request.user) not in allowed_roles:
                return HttpResponseForbidden("Not allowed")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator