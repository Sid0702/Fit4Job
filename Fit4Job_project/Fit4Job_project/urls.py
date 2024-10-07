"""
URL configuration for Fit4Job_project project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ats_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path('about/', about_view, name='about'),
    path('job-list/', job_view, name='job'),
    path('signin/', signin_view, name='signin'),
    path('contact/', contact_view, name='contact'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('hr_dashboard/', hr_dashboard, name='hr_dashboard'),
    path('post_job/', post_job, name='post_job'),
    path('post-job/', post_job, name='post_job'),
    path('hr-dashboard/', hr_dashboard, name='hr_dashboard'),
    path('jobs/', job_view, name='job'),
    path('job/delete/<int:job_id>/', delete_job, name='delete_job'),
    path('job/edit/<int:job_id>/', edit_job, name='edit_job'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),  # Ensure this matches your use

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
