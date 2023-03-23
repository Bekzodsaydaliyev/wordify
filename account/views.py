from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from .forms import SignUpForm
from django.views.generic import CreateView


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog:list')
        return render(request, 'profile/register.html')
    return render(request, 'profile/login.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('account:login')
    return render(request, 'profile/logout.html')


class Register(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'profile/register.html'

