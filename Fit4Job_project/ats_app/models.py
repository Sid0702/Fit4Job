from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)
    is_new_user = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    description = models.TextField(blank=True)
    education = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    experience = models.TextField(blank=True)
    preferred_location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position_applying_for = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv_uploads/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_job_application')
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position_applying_for}"

