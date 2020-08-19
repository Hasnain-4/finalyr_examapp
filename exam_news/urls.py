from django.urls import path
from exam_news import views



urlpatterns = [

    path('news', views.news , name = 'news'),
    path('teacher', views.teacher , name = 'teacher'),
    path('student', views.student , name = 'student'),
    path('delete_question/<post_id>',views.deleteQuestn,name='delete_question'),

    path('teacherquiz', views.teacherquiz , name = 'teacherquiz'),
    path('studentqz', views.studentqz , name = 'studentqz'),
    path('delete_question_quiz/<post_id>',views.deleteQuestnqz,name='delete_question_quiz'),

]