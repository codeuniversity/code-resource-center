from django.db import models

# class Account(models.Model):
    # placeholder attribute!!!
    # first_name = models.CharField(max_length=32)

class UserType(models.Model):
    type_name = models.CharField(max_length=32)

class Institution(models.Model):
    institution_name = models.CharField(max_length=32)

class Department(models.Model):
    department_name = models.CharField(max_length=32)