from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class LongtoShort(models.Model):
    long_url=models.URLField(max_length=500)
    custom_name=models.CharField(max_length=100, unique=True)
    created_date=models.DateField(auto_now_add=True)  #take current date
    vist_count=models.IntegerField(default=0)