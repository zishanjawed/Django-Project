from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator


name_valid = RegexValidator('^[A-Za-z0-9]+(?: +[A-Za-z0-9]+)*$', 'Space before and after name is not allowed.')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

GENDER_CHOICES=(
    ('male','MALE'),
    ('female','FEMALE'),
    ('others','OTHERS')
)

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class People(models.Model):
    name = models.CharField(max_length=100, validators=[name_valid])
    pan_number = models.CharField(max_length=10, unique=True, validators=[alphanumeric])
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    
