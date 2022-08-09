from django.db import models

# Create your models here.

class Contact(models.Model):
  name= models.CharField(max_length=100)
  email= models.EmailField()
  content= models.TextField()
  date= models.DateField()
  project = models.CharField(max_length=100)
  def __str__(self): 
    return self.name