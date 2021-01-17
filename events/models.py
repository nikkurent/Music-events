from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    addrs = models.CharField(max_length=200, null=True, blank=True)
    desc = models.TextField()
    start_date = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    image = models.ImageField(default='event_img/default.jpg', upload_to='event_img')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name