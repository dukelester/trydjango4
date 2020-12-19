from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # photo = models.ImageField(null=False)

    def __str__(self):
        return self.title + '|' + self.author

    def get_absolute_url(self):
        return reverse('home')


class DukeLester(models.Model):
    First_name = models.CharField(max_length=45)
    Middle_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    age = models.IntegerField()
    profile_photo = models.ImageField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=50)

    # email = models.EmailField(null=False)

    def __str__(self):
        return self.First_name + '|' + self.Last_name
