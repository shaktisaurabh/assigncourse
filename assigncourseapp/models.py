from django.db import models

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    instructor=models.CharField(max_length=100)
    rating=models.FloatField() 