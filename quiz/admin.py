from django.contrib import admin
from quiz.models import Teacher_Quiz_Questions,Teacher_Quiz_text

# Register your models here.

#Quiz Section.............

admin.site.register(Teacher_Quiz_text)
admin.site.register(Teacher_Quiz_Questions)