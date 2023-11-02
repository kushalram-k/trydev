from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email, password=password)
            # Perform your login logic here
            return HttpResponse("Login Successful")
        except User.DoesNotExist:
            error = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email, password=password)
        user.save()
        # Perform your registration logic here
        return HttpResponse("Registration Successful")
    return render(request, 'login.html')
