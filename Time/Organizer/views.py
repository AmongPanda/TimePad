from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models.functions import Lower
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
def organization_view(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization')
    else:
        form = OrganizationForm()
    return render(request, '.html', {'form': form})
##############################################################
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = EventForm()
    return render(request, 'main.html', {'form': form})
##############################################################
def participants_view(request):
    if request.method == 'POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participants')
    else:
        form = ParticipantsForm()
    return render(request, '.html', {'form': form})
##############################################################
def ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket')
    else:
        form = TicketForm()
    return render(request, '.html', {'form': form})



