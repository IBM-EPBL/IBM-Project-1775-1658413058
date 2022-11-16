from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin




class UserLevel(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):

        modulename = view_func.__module__
        user = request.user

        if user.is_authenticated:
            if user.user_type == '1':
                if modulename in ['nutra_app.permssions.admin', 'nutra_app.views', 'nutra_app.api.views', 'django.views.static']:
                    pass
            elif user.user_type == '2':
                if modulename in ['nutra_app.permissions.developer','nutra_app.views', 'nutra_app.api.views', 'django.views.static']:
                    pass
            elif user.user_type == '3':
                if modulename in ['nutra_app.permissions.apiusers','nutra_app.views', 'nutra_app.api.views', 'django.views.static']:
                    pass
        else:
            if modulename in ['nutra_app.views',  'nutra_app.api.views', 'django.views.static']:
                pass
            else:
                return None 
















