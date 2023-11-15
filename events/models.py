from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username


class EventCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EventTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(EventTag, blank=True)
    organizer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.user.username} - {self.event.name} Comment'


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user.user.username} - {self.event.name} Rating'


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'{self.user.user.username} - {self.event.name} Notification'


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.event.name} Image'
