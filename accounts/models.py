from django.db import models

# Create your models here.

class Account(models.Model):
    # placeholder attribute!!!
    first_name = models.CharField(max_length=32)

class UserType(models.Model):
    type_name = modelsCharField(max_length=32)

class Institution(models.Model):
    institution_name = modelsCharField(max_length=32)