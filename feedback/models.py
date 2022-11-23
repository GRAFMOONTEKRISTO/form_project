from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()
