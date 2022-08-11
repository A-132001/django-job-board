from random import choices
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify
from jinja2 import ModuleLoader
from django.contrib.auth.models import User
'''
    -html widget
    -validation
    -db size
'''

JOB_TYPES = (
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME'),
)

def image_upload (image_object,image_name):
    name,exten = image_name.split('.')
    return f"Images_of_jobs/{image_object.id}.{exten}"


# Create your models here.
class Job(models.Model):  #table name Job
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  #filed in table named title
    #location 
    job_type = models.CharField(max_length=15,default="",choices=JOB_TYPES)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True)
    image =  models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True,null=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,*kwargs)

class Category(models.Model):
    Category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.Category_name


class Applyers(models.Model):
    job = models.ForeignKey(Job,related_name="apply_job",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    Profile_link = models.URLField()
    cv = models.FileField(upload_to="applyers/")
    coverletter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name