from django.urls import path
from exam1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home , name = 'home'),
    path('sign_up', views.signup , name = 'signup'),
    path('signin', views.signin , name = 'signin'),
    path('forgetpassword', views.forget , name = 'forget'),
    path('about', views.about , name = 'about'),
    path('contact', views.contact , name = 'contact'),
    path('logout', views.logout,name='logout'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('posts', views.posts,name='posts'),
    # path('editimagepost', views.imagepost,name='imagepost'),
    # path('editvideopost', views.videopost,name='videopost'),
    path('editprofile', views.editprofile,name='editprofile'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('dlt/<id>',views.delete_postv,name='dlt'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)