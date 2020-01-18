from django.contrib import admin
from filebrowser.settings import ADMIN_THUMBNAIL
from filebrowser.base import FileObject
from django.utils.html import mark_safe
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Course_Chap_Video,Course_Chapter,Course
# Register your models here.
class VideoCourse(NestedStackedInline):
    model = Course_Chap_Video
    extra = 1
    fk_name = 'course_chap'
class ChapterCourse(NestedStackedInline):
    model = Course_Chapter
    extra = 1
    fk_name = 'course'
    inlines = [VideoCourse]
class PageAdminCourse(NestedModelAdmin):
    def image_thumbnail(self, obj):
        if obj.thumbnail and obj.thumbnail.filetype == "Image":
            return mark_safe('<img src="%s" />' % obj.thumbnail.version_generate(ADMIN_THUMBNAIL).url)
        else:
            return ""
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"
    list_display= ('title','slug','timestamp','image_thumbnail')
    # image_display = AdminThumbnail(image_field=cached_admin_thumb)
    # image_display.short_description = 'Avatar'
    model = Course
    inlines = [ChapterCourse]
    search_fields =['title' , 'brief']
    list_filter = ['title','brief',]
    list_per_page =5
admin.site.register(Course, PageAdminCourse)
admin.site.register(Course_Chap_Video)