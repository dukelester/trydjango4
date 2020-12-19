from django.conf.urls import url
from django.urls import path, include
# from .views import home_view,about_view, index_view
from .views import HomeView, BioData, ArticleDetailView, MyBiodataView, AddPostView, UpdatePostView, \
    DeletepostView ,AddCategoryView # @class based view

urlpatterns = [
    # path('', home_view, name='blog-home'),
    # path('about/', about_view, name='blog-about'),
    # path('index/', index_view, name='index'),
    path('', HomeView.as_view(), name='home'),
    path('about/', BioData.as_view(), name='biodata'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('mydata/<int:pk>', MyBiodataView.as_view(), name='mydata'),
    path('post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', DeletepostView.as_view(), name='delete-post'),
    url('members/', include('django.contrib.auth.urls')),
    url('members/', include('members.urls')),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),

]
