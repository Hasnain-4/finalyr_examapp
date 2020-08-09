from django.db import models
from datetime import datetime , date
from django.utils.timezone import now
from django.contrib.auth.models import User , auth

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length = 222)
    mobile_no = models.CharField(max_length = 222, blank = True)
    message = models.TextField()

    def __str__(self):
        
        return self.name

class Imagepost(models.Model):

    imagename = models.CharField(max_length = 222 , default = None)
    date = models.DateTimeField(default=datetime.now())
    caption = models.CharField(max_length = 2222 , default = None)
    image = models.ImageField(upload_to='post', default = '', blank = True, null=True )

    def __str__(self):
        
        return self.imagename + ' ' + 'added image'

class Videopost(models.Model):

    videoname = models.CharField(max_length = 222 , default = None)
    date = models.DateTimeField(default=datetime.now())
    caption = models.CharField(max_length = 2222 , default = None)
    utube_video_link = models.CharField(max_length = 2222)

    def __str__(self):
        
        return self.videoname +' '+ 'added video'

#In image field .. upload_to section is must
class Userprofile(models.Model):
    profilepic = models.ImageField(upload_to='post/profile',default = 'static/images/hasntravel.jpg')
    about = models.TextField()

    # def __str__(self):
        
    #     return self.username + 'updated profile'