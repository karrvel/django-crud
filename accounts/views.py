from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.EmailBackend import EmailBackend
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"


def showLogin(request):
    return render(request, "registration/login.html")


def Login (request):
    if request.method != 'POST':
        return HttpResponse('Restrcited area!')
    else:
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username and password")
            return HttpResponse("Login failed")

def logout_user(request):
    logout(request)
    return redirect('/')