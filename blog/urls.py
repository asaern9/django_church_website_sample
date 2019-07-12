from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .views import EventView, NewsView, NewsDetailView, AnnouncementView, SermonDetailView, SermonView


urlpatterns = [
    path('', views.index, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog/', views.blog, name='blog-blog'),
    path('blog-detail/', views.blog_detail, name='blog-detail'),
    path('contact/', views.contact, name='blog-contact'),
    path('donate/', views.donate, name='blog-donate'),
    path('event/', EventView.as_view(), name='blog-event'),
    path('news/', NewsView.as_view(), name='blog-News'),
    path('news-detail/<slug>/', NewsDetailView.as_view(), name='blog-news-detail'),
    path('announcement/', AnnouncementView.as_view(), name='blog-announcement'),
    path('sermon/', SermonView.as_view(), name='blog-sermon'),
    path('sermon-detail/<slug>/', SermonDetailView.as_view(), name='blog-sermon-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
