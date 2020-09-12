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

    imagename = models.CharField(max_length = 222 )
    date = models.DateTimeField(default=datetime.now())
    caption = models.CharField(max_length = 2222 , default = None)
    image = models.ImageField(upload_to="pics", default = None, blank = True, null=True )

    def __str__(self):
        
        return self.imagename + ' ' + 'Posted'

class Videopost(models.Model):

    videoname = models.CharField(max_length = 222)
    date = models.DateTimeField(default=datetime.now())
    caption = models.CharField(max_length = 2222 , default = None)
    utube_video_link = models.CharField(max_length = 2222)

    def __str__(self):
        
        return self.videoname +' '+ 'added video'

#In image field .. upload_to section is must
class Userprofile(models.Model):
    profilepic = models.ImageField(upload_to="pics",default = 'static/images/john.jpg')
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False, blank=True)
    about = models.TextField(null=True,blank=True)

    def __str__(self):
        
        return self.user.username + ' ' + 'updated profile'