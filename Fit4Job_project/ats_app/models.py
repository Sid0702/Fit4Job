from django.conf import settings
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user applying for the job
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position_applying_for = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv_uploads/')  # Directory for CV uploads
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp for submission

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position_applying_for}"
