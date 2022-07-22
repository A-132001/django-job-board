from random import choices
from statistics import mode
from tkinter import CASCADE
from django.db import models

'''
    -html widget
    -validation
    -db size
'''

JOB_TYPES = (
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME'),
)


# Create your models here.
class Job(models.Model):  #table name Job
    title = models. CharField(max_length=100)  #filed in table named title
    #location 
    job_type = models.CharField(max_length=15,default="",choices=JOB_TYPES)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.title


class Category(models.Model):
    Category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.Category_name