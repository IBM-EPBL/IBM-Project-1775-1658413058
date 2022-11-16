"""nutra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from nutra_app import views
from nutra_app.functions import database_manual_functions 

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('api/',include('nutra_app.api.urls')),
    path('user-login',views.login_user, name='user-login'),
    path('user-logout',views.logout_user, name='user-logout'),

    path('fruit-classifier',views.predict_fruit, name='fruit-classifier'),

    path('write_foods_csv_file/',database_manual_functions.write_Food_data_csv, name='foods-data-update-csv'),

]
