from turtle import title
from django.db import models

# Create your models here.
class contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()

    def __str__(self):
        return self.first_name

class blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200) 
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title
         
    
