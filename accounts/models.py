from django.db import models
from django.contrib.auth.models import User
# use Django signals to extend User object
from django.db.models.signals import post_save

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
        return self.department_name

class UserRole(models.Model):
    role_name = models.CharField(max_length=32)

    def __str__(self):
        return self.role_name

class UserProfile(models.Model):
    django_user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type_id = models.ForeignKey(UserType, default=6, on_delete=models.SET_DEFAULT)
    institution_id = models.ForeignKey(Institution, default=1, on_delete=models.SET_DEFAULT)
    department_id = models.ForeignKey(Department, default=5, on_delete=models.SET_DEFAULT)
    role_id = models.ForeignKey(UserRole, default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='profile_images', blank=True)

# Create user profile if Django User object has been created.
def create_profile(sender, **kwargs):
    # use keyword argument
    if kwargs['created']:
        user_profile = UserProfile.objects.create(django_user_id=kwargs['instance'])
# connect User and user profile
post_save.connect(create_profile, sender=User)