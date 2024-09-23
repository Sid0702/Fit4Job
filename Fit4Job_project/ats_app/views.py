from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import User
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request, 'main/index.html')

def about_view(request):
    return render(request, 'main/about.html')

def job_view(request):
    return render(request, 'main/job.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def programmer_view(request):
    return render(request, 'main/programmer.html')

def education_view(request):
    return render(request, 'main/education.html')

def design_view(request):
    return render(request, 'main/design.html')

def finance_view(request):
    return render(request, 'main/finance.html')

def production_view(request):
    return render(request, 'main/production.html')

def consult_view(request):
    return render(request, 'main/consult.html')

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

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        # Save the user with a hashed password
        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password, role=role)
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

            # Check if the password is valid
            if check_password(password, user.password):
                # Store user info in the session
                request.session['username'] = user.username
                messages.success(request, 'Sign In successful')
                return redirect('index')
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