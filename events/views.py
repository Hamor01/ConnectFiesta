from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventCreationForm, EventUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


@login_required
def homepage(request):
    try:
        user_profile = request.user.userprofile
    except ObjectDoesNotExist:
        user_profile = None

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'homepage.html', context)


def login_view(request):
    if request.method == 'POST':
        # If the form is submitted
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('homepage')  # Redirect to home or any other page after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        # If it's a GET request, render the login form
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = user.userprofile

    context = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'user_profile.html', context)


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user.userprofile
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_detail', event.id)
    else:
        form = EventCreationForm()

    return render(request, 'create_event.html', {'form': form})


@login_required
def manage_event(request, event_id):
    # Logic to retrieve and display information about the event for management
    event = get_object_or_404(Event, id=event_id, organizer=request.user.userprofile)
    return render(request, 'manage_event.html', {'event': event})


def discover_events(request):
    events = Event.objects.all().order_by('date')
    success_message = messages.get_messages(request)
    if success_message:
        messages.info(request, success_message)
    return render(request, 'discover_events.html', {'events': events})


@login_required
def organizer_dashboard(request):
    # Logic to retrieve and display events created by the logged-in organizer
    user_profile = request.user.userprofile
    created_events = Event.objects.filter(organizer=user_profile)
    return render(request, 'organizer_dashboard.html', {'created_events': created_events})


@login_required
def update_event(request, event_id):
    # Logic to retrieve and update event details
    event = get_object_or_404(Event, id=event_id, organizer=request.user.userprofile)

    if request.method == 'POST':
        form = EventUpdateForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('manage_event', event_id=event.id)
    else:
        form = EventUpdateForm(instance=event)

    return render(request, 'update_event.html', {'form': form, 'event': event})


@login_required
def cancel_event(request, event_id):
    # Logic to cancel an event
    event = get_object_or_404(Event, id=event_id, organizer=request.user.userprofile)

    if request.method == 'POST':
        # Additional logic for confirming event cancellation
        event.delete()
        messages.success(request, 'Event cancelled successfully!')
        return redirect('organizer_dashboard')

    return render(request, 'cancel_event.html', {'event': event})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User registered successfully!')
            return redirect('homepage')  # Redirect to the homepage after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def organizer_events(request):
    user_profile = request.user.userprofile
    events = Event.objects.filter(organizer=request.user.userprofile)

    context = {
        'events': events,
    }

    return render(request, 'organizer_events.html', context)