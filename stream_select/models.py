from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class info(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)


class result(models.Model):
    pass