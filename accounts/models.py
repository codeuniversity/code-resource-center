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
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, blank=True, default=6, on_delete=models.SET_DEFAULT)
    institution = models.ForeignKey(Institution, blank=True, default=1, on_delete=models.SET_DEFAULT)
    department = models.ManyToManyField(Department, blank=True, default=5)
    role = models.ForeignKey(UserRole, blank=True, default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.django_user

# Create user profile if Django User object has been created.
def create_profile(sender, **kwargs):
    # use keyword argument
    if kwargs['created']:
        user_profile = UserProfile.objects.create(django_user=kwargs['instance'])
# connect User and user profile
post_save.connect(create_profile, sender=User)