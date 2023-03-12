from django.contrib import admin

from textbook.models import Course, Tag, Textbook, Syllabus

# Register your models here.
admin.site.register(Tag)
admin.site.register(Textbook)
admin.site.register(Course)
admin.site.register(Syllabus)