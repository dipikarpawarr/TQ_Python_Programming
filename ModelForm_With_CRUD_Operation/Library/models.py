from django.db import models
from django import forms

# Create your models here.
class SignUp_Model(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=10)
    Address = models.CharField(max_length=500)
    EmailAddress = models.EmailField()
    Password = models.CharField(max_length=20)
    class Meta:
        db_table='library_sign_up'

class Login_Model(models.Model):
    EmailAddress = models.EmailField()
    Password = models.CharField(max_length=20)

class Books_Model(models.Model):
    BookName = models.CharField(max_length=100)
    Auther = models.CharField(max_length=100)
    Price = models.IntegerField()
    class Meta:
        db_table = 'Library_Books'

class Issue_Book_Model(models.Model):
    UID = models.IntegerField()
    BookName = models.CharField(max_length=100)
    IssuedDate = models.DateField()
    ReturnDate = models.DateField()
    class Meta:
        db_table = 'library_take_book'

class Return_Book_Model(models.Model):
    UID = models.IntegerField()
    BookName = models.CharField(max_length=100)
