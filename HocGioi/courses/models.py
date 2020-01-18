from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from HocGioi.utils import generate_unique_slug
from filebrowser.fields import FileBrowseField
from tinymce import HTMLField
import requests
# Create your models here.
class Course(models.Model):
    title = models.CharField("Tên Khoá học", max_length=400)
    brief = models.TextField(verbose_name='Tóm Tắt')
    slug = models.SlugField(unique=True,editable=False , blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = FileBrowseField("Image", max_length=5000, directory="uploads/", extensions=[".jpg",".jpeg",".png"], blank=True)
    overview  = HTMLField('Nội Dung')
    featured = models.BooleanField("Hiện thị",default = True)
    class Meta:
        
        verbose_name_plural = "Khoá Học"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
       return self.title
    def save(self, *args, **kwargs):
        if self.slug:  
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Course, self.title)
        else: 
            self.slug = generate_unique_slug(Course, self.title)
        super(Course,self).save()
class Course_Chapter(models.Model):
    title = models.CharField("Tên Khoá học", max_length=400)
    course = models.ForeignKey(Course,related_name='chap', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Lộ trình"
        verbose_name_plural = "Lộ trình"
class Course_Chap_Video(models.Model):
    type = [
        ('GD', 'Google Drive'),
        ('YT', 'Youtube'),
        ('IR', 'iframe'),
    ]
    title = models.CharField("Tên video", max_length=400)
    type_video = models.CharField('Kiểu video',choices = type, max_length=2000)
    url = models.CharField("URL", max_length=501)
    url_api  = models.CharField(editable=False , blank = True,max_length=2000)
    url_thumb  = models.CharField(blank = True,editable=False, max_length=50)
    time_video_mili = models.IntegerField(blank = True,editable=False)
    is_open_for_free  = models.BooleanField(default=True)
    course_chap = models.ForeignKey(Course_Chapter,related_name='video', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video Khoá Học"

    def __str__(self):
        return self.title
    def save(self):
        if self.type_video=="GD":
            if self.url.find("drive.google") != -1:
                get_id = self.url.strip('@https?://(?:[\w\-]+\.)*(?:drive|docs)\.google\.com/(?:(?:folderview|open|uc)\?(?:[\w\-\%]+=[\w\-\%]*&)*id=|(?:folder|file|document|presentation)/d/|spreadsheet/ccc\?(?:[\w\-\%]+=[\w\-\%]*&)*key=)([\w\-]{28,})')
                KEY = "AIzaSyAoX3E4y1ZywvoSoqSiJWcxQHxGjlI6wyg"
                LINK = "https://www.googleapis.com/drive/v3/files/"
                
                rs = requests.get(LINK+get_id+"?fields=*&key="+KEY)
                data = rs.json()
                
                self.time_video_mili = int(data['videoMediaMetadata']['durationMillis'])
                    
                if data['hasThumbnail'] == True:
                    self.url_thumb = data['thumbnailLink']
                self.url_api = LINK+get_id+"?alt=media&key="+KEY
        super(Course_Chap_Video,self).save()





