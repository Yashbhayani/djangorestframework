from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

class Book(models.Model):
    Bookname = models.CharField(max_length=100)
    Price = models.IntegerField()
    