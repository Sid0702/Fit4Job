from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Import login_required
from django.views.decorators.csrf import csrf_protect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'main/index.html')

def about_view(request):
    return render(request, 'main/about.html')

@login_required(login_url='signin')  # Add login_required to protect the job page
def job_view(request):
    return render(request, 'main/job.html')

def contact_view(request):
    return render(request, 'main/contact.html')


def HR_view(request):
    return render(request, 'main/HR.html')

def post_view(request):
    return render(request, 'main/post.html')

@login_required(login_url='signin')  # Protect individual job category pages
def programmer_view(request):
    return render(request, 'main/programmer.html')

@login_required(login_url='signin')
def education_view(request):
    return render(request, 'main/education.html')

@login_required(login_url='signin')
def design_view(request):
    return render(request, 'main/design.html')

@login_required(login_url='signin')
def finance_view(request):
    return render(request, 'main/finance.html')

@login_required(login_url='signin')
def production_view(request):
    return render(request, 'main/production.html')

@login_required(login_url='signin')
def consult_view(request):
    return render(request, 'main/consult.html')

# @csrf_protect
# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         role = request.POST['role']
        
#         # Validation
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')

#         # Check if the username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#             return redirect('register')
        
#         # Check if the email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already registered')
#             return redirect('register')

#         # Save the user with a hashed password
#         hashed_password = make_password(password)
#         user = User(username=username, email=email, password=hashed_password, role=role)
#         user.save()

#         messages.success(request, 'Registration successful. Please sign in.')
#         return redirect('signin')

#     return render(request, 'main/register.html')


# @csrf_protect
# def signin_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)

#             # Check if the password is valid
#             if check_password(password, user.password):
#                 # Store user info in the session
#                 request.session['username'] = user.username
#                 messages.success(request, 'Sign In successful')

#                 # Redirect to 'next' if it exists in the GET parameters
#                 next_url = request.GET.get('job')
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return redirect('index')
#             else:
#                 messages.error(request, 'Invalid password')
#         except User.DoesNotExist:
#             messages.error(request, 'User does not exist')

#     return render(request, 'main/signin.html')

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'Logged out successfully')
#     return redirect('signin')
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
            if check_password(password, user.password):
                # Store user info in the session
                request.session['username'] = user.username
                messages.success(request, 'Sign In successful')
                return redirect('job')  # Redirect to job view after successful sign in
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
    return render(request, 'main/job.html')