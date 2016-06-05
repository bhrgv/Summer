from __future__ import unicode_literals

from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=225)
    created = models.DateField()
    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List)
    description = models.TextField()
    due_date=models.DateField()
    completed = models.BooleanField()
