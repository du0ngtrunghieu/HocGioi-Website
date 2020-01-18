from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    post_trend = Post.objects.filter(featured = True).order_by('timestamp')[:5]
    post_all = Post.objects.filter(featured = True).order_by('timestamp')
    context = {
        'data_trend':post_trend,
        'data_post':post_all
    }
    return render(request,"index-blog.html",context)
def pathBlog(request,slug):
    data = get_object_or_404(Post,slug = slug)
    context ={
        'data':data
    }
    return render(request,'post-detail.html',context)