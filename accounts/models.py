from django.db import models
# use Django signals to extend User object
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

###### USER MANAGER ######
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email.")
        if not first_name:
            raise ValueError("Users must have a first name.")
        if not last_name:
            raise ValueError("User must have a last name.")
        if not password:
            raise ValueError("User must have a password.")
        user_obj = self.model(
            # make email case-insensitive
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                first_name=first_name,
                last_name = last_name,
        )
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                is_admin=True,
                first_name = first_name,
                last_name = last_name,
        )
        return user

###### CUSTOM USER MODEL ######
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True) # can login
    staff = models.BooleanField(default=False) # staffuser
    admin = models.BooleanField(default=False) # superuser
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' # make email the username
    # username_field, ws and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    # "Does the user have a specific permission?"
    def has_perm(self, perm, obj=None):
        return True

    # "Does the user have permissions to view the app `app_label`?"
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

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
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.SET_NULL)
    institution = models.ForeignKey(Institution, null=True, on_delete=models.SET_NULL)
    # department = models.ManyToManyField(Department)
    role = models.ForeignKey(UserRole, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)

    def __str__(self):
        return self.django_user

# Trigger creation of corresponding user profile as soon as Django User object has been created.
def create_profile(sender, **kwargs):
    # use keyword argument
    if kwargs['created']:
        user_profile = UserProfile.objects.create(django_user=kwargs['instance'])
# connect User and user profile
        post_save.connect(create_profile, sender=User)
        return self.department_name
