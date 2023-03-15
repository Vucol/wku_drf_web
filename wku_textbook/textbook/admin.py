from django.contrib import admin

from textbook.models import Course, BookTag, Textbook, Syllabus

# Register your models here.
admin.site.register(BookTag)
admin.site.register(Textbook)
admin.site.register(Course)
admin.site.register(Syllabus)