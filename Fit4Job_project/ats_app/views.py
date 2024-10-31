
import re
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Import login_required
from django.views.decorators.csrf import csrf_protect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from .models import Job
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone

def index(request):
    return render(request, 'main/index.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def hr_dashboard(request):
    if request.session.get('role') == 'recruiter':
        user = User.objects.get(username=request.session.get('username'))
        jobs = Job.objects.filter(user=user.id)
        return render(request, 'main/hr_dashboard.html', {'jobs': jobs})
    else:
        messages.error(request, 'Access denied. HR only.')
        return redirect('job')

def post_job(request):
    if request.method == 'POST':
        title = request.POST['job_title']
        description = request.POST['job_description']
        job_type = request.POST['job_type']
        location = request.POST['location']
        skills = request.POST['skills']
        salary = request.POST['salary']

        # Handle multiple delimiters (comma, space, newline)
        skill_list = re.split(r'[,\s\n]+', skills.strip()) if skills else []
        skills_cleaned = ', '.join(skill_list)  # Join the cleaned skill list
        user = User.objects.get(username=request.session.get('username'))

        # Save job post with cleaned skills
        job = Job(title=title, description=description, job_type=job_type, location=location, skills=skills_cleaned, salary=salary,user=user)
        job.save()
        messages.success(request, 'Job posted successfully!')
        return redirect('hr_dashboard')
    
    return render(request, 'main/job_form.html')

@csrf_protect
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']
        
        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        # Save the user with a hashed password
        
        hashed_password = make_password(password)
        user = User.objects.create(username=username, email=email, password=hashed_password, role=role)
        user.save()
        messages.success(request, 'Registration successful. Please sign in.')
        return redirect('signin')

    return render(request, 'main/register.html')


@csrf_protect
def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # Store user info in the session, including the role
                request.session['username'] = user.username
                request.session['user_id'] = user.id
                request.session['role'] = user.role
                messages.success(request, 'Sign In successful')

                if user.role == 'recruiter':
                    return redirect('hr_dashboard')  # Redirect HR users to the HR dashboard
                else:
                    return redirect('index')  # Redirect other users to job view

            else:
                messages.error(request, 'Invalid password')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

    return render(request, 'main/signin.html')

def logout_view(request):
    # Clear the session data
    request.session.flush()
    messages.success(request, 'Logged out successfully')
    return redirect('signin')

# Middleware to check if user is authenticated
def is_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if 'username' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'You need to log in to access this page.')
            return redirect('signin')
    return wrapper

# Apply the decorator to the job view
@is_authenticated
def job_view(request):
    query = request.GET.get('q', '')  # Search query
    today = timezone.now().date() # Current date for checking new jobs

    # Filter jobs based on search query for title, location, salary, and skills
    job_list = Job.objects.filter(
        Q(title__icontains=query) |           # Search by title
        Q(location__icontains=query) |        # Search by location
        Q(salary__icontains=query) |          # Search by salary
        Q(skills__icontains=query)            # Search by skills
    ) if query else Job.objects.all()

    job_list = job_list.order_by('-created_at')

    # Pagination logic (show 5 jobs per page)
    paginator = Paginator(job_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template with the paginated jobs and the search query
    return render(request, 'main/job_list.html', {
        'page_obj': page_obj,
        'query': query,
        'today': today
    })
    # return render(request, 'main/job_list.html', {'jobs': jobs})

def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    messages.success(request, 'Job deleted successfully!')
    return redirect('hr_dashboard')

def edit_job(request, job_id):
    job = Job.objects.get(id=job_id)
    
    if request.method == 'POST':
        job.title = request.POST['job_title']
        job.description = request.POST['job_description']
        job.job_type = request.POST['job_type']
        job.location = request.POST['location']
        skills = request.POST['skills']
        job.salary = request.POST['salary']

        # Handle multiple delimiters (comma, space, newline)
        skill_list = re.split(r'[,\s\n]+', skills.strip()) if skills else []
        job.skills = ', '.join(skill_list)  # Update the cleaned skill list

        job.save()
        
        messages.success(request, 'Job updated successfully!')
        return redirect('hr_dashboard')
    
    return render(request, 'main/edit_job.html', {'job': job})

def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    print(f"Rendering apply_form.html for job: {job.title}")
    
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get('username'))
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        position_applying_for = request.POST.get('position-applying-for')
        message = request.POST.get('message')
        cv = request.FILES.get('cv')

        # Create the application
        job = JobApplication.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            position_applying_for=position_applying_for,
            message=message,
            cv=cv
        )
        job.save()
        print("Applied")
        # Redirect to a success page or job listing
        return redirect('job')  # Change this to your desired URL after successful submission

    return render(request, 'main/apply_form.html', {'job': job})

# def user_job_list(request):

#     user_jobs = Job.objects.filter(user=user)  # Assuming you have a 'posted_by' field in Job model
#     return render(request, 'main/job_list.html', {'user_jobs': user_jobs})

def applicant_view(request):
    if request.session.get('role') == 'recruiter':
        user = User.objects.get(username=request.session.get('username'))
        jobs = Job.objects.filter(user=user)
    else:
        messages.error(request, 'Access denied. HR only.')
        return redirect('job')

    return render(request, 'main/applicants.html', {"jobs": jobs})


def job_detail(request, job_id):
    # Get the specific job by ID or return 404 if not found
    job = get_object_or_404(Job, id=job_id)
    
    # Render the job detail template
    return render(request, 'main/job_detail.html', {'job': job})

def profile_view(request):
    if 'username' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        profile, created = Profile.objects.get_or_create(user=user)

        if request.method == 'POST':
            # Update profile fields directly from the request
            profile.full_name = request.POST.get('full_name')
            profile.phone_number = request.POST.get('phone_number')
            profile.description = request.POST.get('description')
            profile.education = request.POST.get('education')
            profile.skills = request.POST.get('skills')
            profile.experience = request.POST.get('experience')
            profile.preferred_location = request.POST.get('preferred_location')

            # Handle profile picture upload
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            # Update email if it has changed (optional)
            email = request.POST.get('email')
            if email and email != request.user.email:
                request.user.email = email
                request.user.save()

            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')

        context = {
            'profile': profile,
        }
        return render(request, 'main/profile.html', context)

    # Redirect to login if the user is not authenticated
    messages.warning(request, 'You need to be logged in to view your profile.')
    return redirect('signin')