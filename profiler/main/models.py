from django.db import models

# Create your models here.
class Accountusers(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=100)
    
