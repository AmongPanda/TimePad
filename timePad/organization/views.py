from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from  organization.forms import *
from django.urls import reverse_lazy


def main(request):
    events = Event.objects.order_by('-date')
    return render(request, 'main.html', {'events': events})


##############################################################
def events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = EventForm()
    return render(request, 'events.html', {'form': form})


##############################################################

def user_org(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserOrgForm()
    return render(request, 'registration.html', {'form': form})
def tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TicketForm()
    return render(request, 'tickets.html', {'form': form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'organization/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'organization/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')

