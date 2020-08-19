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

class Stud(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False, blank=True)
    answer = models.TextField()
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=True)
    def __str__(self): 
        return self.user.username


class TecherData(models.Model):

    writtenquestion = models.CharField(default='',max_length= 330, blank = True, null=True )
    imagequestion = models.ImageField(upload_to="pics", default = '', blank = True, null=True )
    option1 = models.CharField(default='A',max_length= 150)
    option2 = models.CharField(default='B',max_length= 150)
    option3 = models.CharField(default='C',max_length= 150)
    option4 = models.CharField(default='D',max_length= 150)

# class StudentResult(models.Model):

#     stdname = models.CharField(max_length=255,blank=True,null=True)
#     answer = models.TextField()
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=True)
#     def __str__(self): 
#         return self.user+ ' ' + 'Submitted'
    
    # To store the data with registered username.......
    

# class StudentSubmitResult(models.Model):
#     stname = models.CharField(default='Student' ,max_length= 150)
#     answer = models.TextField()

# #if we remove this str then data will be save as object data .. and this str giving blank value
#     def __str__(self):
#         return self.stname
    
    

#....................Quiz Section..................

class Teacher_Quiz_text(models.Model):
    
    timeslot = models.CharField(max_length= 150)
    subject = models.CharField(max_length= 150)
    bestwish = models.CharField(default=None,max_length= 350, blank = True, null=True )
    warningmessage = models.CharField(default=None,max_length= 550, blank = True, null=True )
    date = models.DateTimeField(default=datetime.now())
        
    def __str__(self):
        return self.subject + ' ' + 'Question'


class Teacher_Quiz_Questions(models.Model):

    writtenquestion = models.CharField(default='',max_length= 330, blank = True, null=True )
    imagequestion = models.ImageField(upload_to="pics", default = '', blank = True, null=True )
    option1 = models.CharField(default='A',max_length= 150)
    option2 = models.CharField(default='B',max_length= 150)
    option3 = models.CharField(default='C',max_length= 150)
    option4 = models.CharField(default='D',max_length= 150)


class StudentSubmitQuiz(models.Model):
    answer = models.TextField()
    user = models.OneToOneField(User, models.CASCADE)
