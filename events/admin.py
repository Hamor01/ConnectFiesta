from django.contrib import admin
from .models import UserProfile, Event, EventCategory, EventTag, Comment, Rating, Notification, EventImage

admin.site.register(UserProfile)
admin.site.register(EventCategory)
admin.site.register(EventTag)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Notification)
admin.site.register(EventImage)
