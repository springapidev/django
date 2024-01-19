from django.db import models


# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    COUNTRY_CHOICES = [
        ('bd', 'Bangladesh'),
        ('jp', 'Japan'),
        ('us', 'USA')
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    comments = models.TextField()
    birth_date = models.DateField()


def __str__(self):
    return self.name
