from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=90)
    roll = models.IntegerField()
    marks = models.IntegerField()
    city = models.CharField(max_length=90)
    tour_place = models.CharField(max_length=90)
    dream = models.CharField(max_length=120)
    college = models.CharField(max_length=150)
    ideology = models.CharField(max_length=90)
    occupation = models.CharField(max_length=90, null=True)
    
    
    def __str__(self):
        return self.name
    