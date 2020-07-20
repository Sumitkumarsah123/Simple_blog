
from django.urls import path
from .views import BlogListView,BlogDetailView
from . import views
urlpatterns=[

    # path('', views.home, name='home'),
   # path('', views.blog, name='blog'),
    path('', BlogListView.as_view(), name='Blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),

    # path('blog', views.blog, name='blog'),
    path('create', views.create, name='create'),

    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('search', views.search ,name='search'),
    # path('blog_details/<int:id>', views.blog_details, name='blog_details'),
    path('feedback', views.feedback ,name='feedback'),
    


    

]