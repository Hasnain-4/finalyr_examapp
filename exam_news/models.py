from django.db import models
from datetime import datetime , date
from django.contrib.auth.models import User , auth

# Create your models here.

class Teacher(models.Model):
    
    timeslot = models.CharField(max_length= 150)
    subject = models.CharField(max_length= 150)
    bestwish = models.CharField(default=None,max_length= 350, blank = True, null=True )
    warningmessage = models.CharField(default=None,max_length= 550, blank = True, null=True )
    date = models.DateTimeField(default=datetime.now())
        
    def __str__(self):
        return self.subject + ' ' + 'Question'

class TecherData(models.Model):

    writtenquestion = models.CharField(default='',max_length= 330, blank = True, null=True )
    imagequestion = models.ImageField( default = None, blank = True, null=True )
    option1 = models.CharField(default='A',max_length= 150)
    option2 = models.CharField(default='B',max_length= 150)
    option3 = models.CharField(default='C',max_length= 150)
    option4 = models.CharField(default='D',max_length= 150)

# class StudentData(models.Model):

#     stdname = models.CharField(max_length=255,blank=True,null=True)
#     answer = models.CharField(max_length=255,blank=True,null=True)
    
#     # To store the data with registered username.......
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=True)
    
#     def __str__(self): 
#         return self.user+ ' ' + 'Submitted'

class StudentSubmit(models.Model):
    answer = models.TextField()
    user = models.OneToOneField(User, models.CASCADE)

#if we remove this dtr then data will be save as object data .. and this str giving blank value
    def __str__(self):
        return self.user.username
    

   
    

    
