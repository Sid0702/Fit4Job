"""
URL configuration for Fit4Job_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from ats_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path('about/', about_view, name='about'),
    path('job/', job_view, name='job'),
    path('signin/', signin_view, name='signin'),
    path('contact/', contact_view, name='contact'),
    path('programmer/', programmer_view, name='programmer'),
    path('education/', education_view, name='education'),
    path('design/', design_view, name='design'),
    path('finance/', finance_view, name='finance'),
    path('production/', production_view, name='production'),
    path('consult/', consult_view, name='consult'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('HR/', HR_view, name='HR'),
]
