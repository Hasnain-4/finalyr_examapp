from django.urls import path
from exam_news import views



urlpatterns = [

    path('news', views.news , name = 'news'),
    path('search', views.search , name = 'search'),
    path('teacher', views.teacher , name = 'teacher'),
    path('student', views.student , name = 'student'),
    path('delete_question/<post_id>',views.deleteQuestn,name='delete_question'),

]