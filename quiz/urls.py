from django.urls import path
from quiz import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

        path('start_quiz/',views.welcome, name="start_quiz"),
        path('quiz/',views.index, name="quiz"),
        path('save_ans/',views.save_ans,name="saveans"),
        path('result/',views.result,name="result"),

        #  path('teacherquiz', views.teacherquiz , name = 'teacherquiz'),
        # path('studentqz', views.studentqz , name = 'studentqz'),
        # path('delete_question_quiz/<post_id>',views.deleteQuestnqz,name='delete_question_quiz'),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    