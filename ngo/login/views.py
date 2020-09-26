

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login as login_auth
from django.views.generic import CreateView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def home(request):
    context = {}
    return render(request, 'login/main.html', context)


class NgoSignUpView(CreateView):
    model = User
    form_class = NgoSignUpForm
    template_name = 'login/ngo_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ngo'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login_auth(self.request, user)
        return redirect('main:ngo_tabular', user.id)


class DonorSignUpView(CreateView):
    model = User
    form_class = DonorSignUpForm
    template_name = 'login/donor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'donor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login_auth(self.request, user)
        return redirect('home')


def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            if user.is_ngo:
                login_auth(request, user)
                return redirect('main:ngo_tabular')
            else:
                messages.info(request, 'Ngo is not registered')
            if user.is_donor:
                login_auth(request, user)
                return redirect('donor')
            else:
                messages.info(request, 'User is not registered')

        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'login/login.html', context)


def ngo(request):
    context = {}
    return render(request, 'login/ngo.html', context)


def donor(request):
    context = {}
    return render(request, 'login/donor.html', context)
