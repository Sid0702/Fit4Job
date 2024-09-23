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

def register_view(request):
    return render(request, 'main/register.html')