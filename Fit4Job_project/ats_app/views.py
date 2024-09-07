from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about_view(request):
    return render(request, 'main/about.html')

def job_view(request):
    return render(request, 'main/job.html')

def signin_view(request):
    return render(request, 'main/signin.html')

def contact_view(request):
    return render(request, 'main/contact.html')


