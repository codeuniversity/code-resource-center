from django.db import models

# Create your models here.

class Account(models.Model):
    # placeholder attribute:
    first_name = models.CharField(max_length=32)