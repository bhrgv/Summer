from __future__ import unicode_literals

from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=225)
    acronym = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=225)
    college = models.ForeignKey(College)
    dbfolder = models.CharField(max_length=100)
    dropout = models.BooleanField(default=False)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Marks(models.Model):
    name = models.ForeignKey(Student)
    transform = models.IntegerField()
    from_custom_base26 = models.IntegerField()
    get_pig_latin = models.IntegerField()
    top_chars = models.IntegerField()
    total =models.IntegerField()

    def __str__(self):
        return self.name.name

class Teacher(models.Model):
    name = models.CharField(max_length=225)
    college = models.ForeignKey(College)

    def __str__(self):
        return self.name