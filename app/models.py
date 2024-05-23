from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=100)
    sage = models.IntegerField()
    semail = models.EmailField()
    spassword = models.CharField(max_length=100)
    address = models.TextField()
    hubby = models.CharField(max_length=100)
    school_type = models.CharField(max_length=50)
    school_logo = models.FileField(upload_to='logos/')

    def __str__(self):
        return self.sname


