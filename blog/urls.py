from django.urls import path
from .views import home_view,about_view, index_view

urlpatterns = [
   path('', home_view, name='blog-home'),
   path('about/', about_view, name='blog-about'),
   path('index/', index_view, name='index'),
]
