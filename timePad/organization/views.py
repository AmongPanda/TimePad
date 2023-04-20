
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import *
from .forms import *

def main(request):
    events = Event.objects.all()
    now = timezone.now()
    context = {
        'now': now,
        'events': events
    }
    return render(request, 'main.html', context)

##############################################################
def events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = EventForm()
    return render(request, 'main.html', {'form': form})
##############################################################

def user_org(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participants')
    else:
        form = UserOrgForm()
    return render(request, '.html', {'form': form})

##############################################################
def tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket')
    else:
        form = TicketForm()
    return render(request, '.html', {'form': form})

