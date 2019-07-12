from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.


class News(models.Model):
    published_date = models.DateTimeField()
    reporter = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    content = models.TextField()
    picture = models.ImageField(upload_to='News/')
    slug = models.SlugField(default='news-item')

    def get_absolute_url(self):
        return reverse('blog-news-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Event(models.Model):
    date = models.DateTimeField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    content = models.TextField()
    picture = models.ImageField(upload_to='Event/')

    def __str__(self):
        return self.title


class Sermon(models.Model):
    date_of_sermon = models.DateTimeField()  # only the month and the day
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    format_video = models.FileField(upload_to='Sermon/Video/', blank=True, null=True)
    format_audio = models.FileField(upload_to='Sermon/Audio/', blank=True, null=True)
    format_doc = models.FileField(upload_to='Sermon/Document/', blank=True, null=True)
    picture = models.ImageField(upload_to='Sermon/pictures', null=True)
    title = models.CharField(max_length=100)
    preacher = models.CharField(max_length=150)
    category = models.CharField(max_length=50, null=True)
    content = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title + ' _____' + self.preacher

    def get_absolute_url(self):
        return reverse('blog-sermon-detail', kwargs={'slug': self.slug})


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.full_name + " ---------  " + self.email


class Gallery(models.Model):
    gallery = models.ImageField(upload_to='Gallery/')

    def __str__(self):
        return self.gallery.name
