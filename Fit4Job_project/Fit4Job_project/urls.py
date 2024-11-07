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
    path('applicant', applicant_view, name='applicant'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),

    path('profile/', profile_view, name='profile'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)