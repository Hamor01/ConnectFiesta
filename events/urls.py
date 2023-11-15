from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('cancel_event/', cancel_event, name='cancel_event'),
    path('create_event/', create_event, name='create_event'),
    path('discover_events/', discover_events, name='discover_events'),
    path('login/', login_view, name='login'),
    path('manage_event/', manage_event, name='manage_event'),
    path('organizer_dashboard/', organizer_dashboard, name='organizer_dashboard'),
    path('organizer_events/', organizer_events, name='organizer_events'),
    path('register/', register, name='register'),
    path('update_event/', update_event, name='update_event'),
]
