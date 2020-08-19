from django.contrib import admin
from exam_news.models import Teacher, Stud, TecherData,Teacher_Quiz_Questions,Teacher_Quiz_text,StudentSubmitQuiz

# Register your models here.
admin.site.register(Teacher)
admin.site.register(TecherData)
admin.site.register(Stud)

#Quiz Section.............

admin.site.register(Teacher_Quiz_text)
admin.site.register(Teacher_Quiz_Questions)
admin.site.register(StudentSubmitQuiz)
