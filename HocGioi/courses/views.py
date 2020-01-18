from django.shortcuts import render,get_object_or_404
from .models import Course,Course_Chap_Video
from django.http import JsonResponse
import requests
import urllib

# Create your views here.
def Course_Path(request):
    # header={
        
    #     'Content-Type': 'application/json',
    #     'Cache-Control': 'no-cache, no-store, must-revalidate'
    
    #  }
    # rs = requests.get("https://mail.google.com/e/get_video_info?docid=0BzP-w0lYJ6ifcF9BdWdBSTUwUEE")
    # t1 = urllib.parse.unquote(rs.text)
    # co = rs.cookies.get_dict()
    # cookies = co
    rs2 = requests.get("https://mail.google.com/e/get_video_info?docid=0BzP-w0lYJ6ifcF9BdWdBSTUwUEE")
    t2 = urllib.parse.unquote(rs2.text)
    context ={
        'data':t2
        
    }
    return render(request,"course_path.html",context)
def Course_Into(request,slug):
    data = get_object_or_404(Course,slug = slug)
    context = {
        'data' : data
    }

    return render(request,"course_into.html",context)
def Course_Lesson(request,slug):
    course = get_object_or_404(Course,slug = slug)

    context = {
        'course':course,
    }
    return render(request ,"course_lesson.html",context)
def Course_getVideo(request,id):
    
    if id:
        obj = get_object_or_404(Course_Chap_Video , id = id)
        data = {
            'link':obj.url_api,
            'thumb':obj.url_thumb,
            'title':obj.title,
        }
    return JsonResponse(data)