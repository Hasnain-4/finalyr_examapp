from django.db import models
from datetime import datetime , date


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
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.writtenquestion
