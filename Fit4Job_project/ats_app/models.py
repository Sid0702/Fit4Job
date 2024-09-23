from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Ensure you use hashing in a real implementation
    role = models.CharField(max_length=50, choices=[('job_seeker', 'Job Seeker'), ('recruiter', 'Recruiter')])

    def __str__(self):
        return self.username