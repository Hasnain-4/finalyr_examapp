from django.urls import path
from exam_news import views



urlpatterns = [

    path('news', views.news , name = 'news'),
    path('teacher', views.teacher , name = 'teacher'),
    path('student', views.student , name = 'student'),

]