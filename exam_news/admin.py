from django.contrib import admin
from exam_news.models import Teacher, StudentData, TecherData

# Register your models here.
admin.site.register(Teacher)
admin.site.register(TecherData)
admin.site.register(StudentData)
