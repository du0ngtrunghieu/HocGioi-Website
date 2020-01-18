
from django.urls import path,include
from .views import home,pathBlog
app_name="blogs"
urlpatterns = [
    path('',home,name="blog-home"),
    path('<slug:slug>/',pathBlog, name="post-detail"),
    
]