from django.db import models

# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.email