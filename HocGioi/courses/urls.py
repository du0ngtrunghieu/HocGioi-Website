
from django.urls import path,include
from .views import Course_Path,Course_Lesson,Course_getVideo,Course_Into
app_name="course"
urlpatterns = [
    path('',Course_Path,name="course_path" ),
    path('<slug:slug>/',Course_Into, name="course_into"),
    path('<slug:slug>/learn/',Course_Lesson, name="course_lesson"),
    path('getAPI-video/<int:id>',Course_getVideo,name="course_video")
]