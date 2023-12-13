
# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
