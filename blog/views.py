from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Gallery
from django.views.generic import ListView, DetailView
from .admin import *

# Create your views here.


def about(request):
    return render(request, 'blog/about.html')


def blog(request):
    return render(request, 'blog/blog.html')


def blog_detail(request):
    return render(request, 'blog/blog-details.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            messages.info(request, "Message submitted")
            return redirect('blog-contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def donate(request):
    return render(request, 'blog/donate.html')


class AnnouncementView(ListView):
    model = Announcement
    paginate_by = 5
    template_name = 'blog/announcement.html'


class NewsView(ListView):
    model = News
    paginate_by = 5
    template_name = 'blog/News.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news-detail.html'


class EventView(ListView):
    model = Event
    paginate_by = 5
    template_name = 'blog/events.html'


def index(request):
    sermon = Sermon.objects.all().order_by('-id')[:3]
    gallery = Gallery.objects.all()
    event = Event.objects.all().order_by('-id')[:4]
    news = News.objects.all().order_by('-id')[:3]
    context = {'sermon': sermon, 'event': event, 'news': news, 'gallery': gallery}
    return render(request, 'blog/index.html', context)


class SermonView(ListView):
    model = Sermon
    paginate_by = 1
    template_name = 'blog/sermons.html'


class SermonDetailView(DetailView):
    model = Sermon
    template_name = 'blog/sermons-details.html'
