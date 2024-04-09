from django.db import models

# Create your models here.
class test(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    DOJ =models.DateField(null=True)

class demo(models.Model):
    department = models.CharField(max_length = 50)
    salary = models.IntegerField()

    