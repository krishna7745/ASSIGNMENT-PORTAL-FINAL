from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class regis(models.Model):
    enroll=models.CharField(max_length=10)
    name= models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    course=models.CharField(max_length=10)
    sem=models.IntegerField()
    q1=models.IntegerField(default=0)
    q2=models.IntegerField(default=0)
    q3=models.IntegerField(default=0)
    q4=models.IntegerField(default=0)
    q5=models.IntegerField(default=0)
    q6=models.IntegerField(default=0)
    q7=models.IntegerField(default=0)
    q8=models.IntegerField(default=0)
    q9=models.IntegerField(default=0)
    q10=models.IntegerField(default=0)
class ques(models.Model):
    quesno=models.IntegerField(default=0)
    sem=models.IntegerField(default=6)
    ques=models.CharField(max_length=1000)
    i=models.CharField(max_length=100)
    o=models.CharField(max_length=100)

