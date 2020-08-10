from django.urls import path
from exam_news import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('news', views.news , name = 'news'),
    path('teacher', views.teacher , name = 'teacher'),
    path('student', views.student , name = 'student'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)