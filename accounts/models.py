from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.type_name

class Institution(models.Model):
    institution_name = models.CharField(max_length=32)

    def __str__(self):
        return self.institution_name

class Department(models.Model):
    department_name = models.CharField(max_length=32)

    def __str__(self):
        return self.institution_name

class UserRole(models.Model):
    role_name = models.CharField(max_length=32)

    def __str__(self):
        return self.role_name

class UserProfile(models.Model):
    django_user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type_id = models.ForeignKey(UserType, on_delete=models.SET_DEFAULT)
    institution_id = models.ForeignKey(Institution, default=2, on_delete=models.SET_DEFAULT)
    role_id = models.ForeignKey(UserRole, default=2, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='profile_images', blank=True)