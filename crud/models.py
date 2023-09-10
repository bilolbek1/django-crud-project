from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    city = models.CharField(max_length=54)
    b_date = models.DateField()
    job = models.CharField(max_length=32)

    def __str__(self):
        return self.name

