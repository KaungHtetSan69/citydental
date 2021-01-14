from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact.html/',views.contact,name='contact'),
    path('service.html/',views.services,name='services'),
    path('about.html/',views.about,name='about'),
    path('pricing.html',views.pricing,name='pricing'),
    path('blog.html',views.blog1,name='blog'),
    path('blog-details.html',views.blog2,name='blog-details')
]