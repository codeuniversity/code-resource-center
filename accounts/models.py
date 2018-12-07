from django.db import models
from django.forms.models import model_to_dict
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
    
    def initials(self):
        initials = self.first_name[:1].upper() + self.last_name[:1].upper()
        return initials

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

class Department(models.Model):
    department_name = models.CharField(max_length=32)
    
    def __str__(self):
        return self.department_name
    
class Profile(models.Model):
 # Institution enums
    CODE = 'CODE'
    CD = 'CD'
    OTHER = 'OTHER'
    INSTITUTION_CHOICES = (
        (CODE, 'CODE University Berlin'),
        (CD, 'Code+Design Camps'),
        (OTHER, 'other'),
    )

    # occupation enums
    STUDENT = 'STUDENT'
    AC_STAFF = 'AC_STAFF'
    ADMIN_STAFF = 'ADMIN_STAFF'
    ALUMNI = 'ALUMNI'
    EXTERNAL = 'EXTERNAL'

    OCCUPATION_CHOICES = (
        (STUDENT, 'Student'),
        (CD, 'Code+Design Camper'),
        (AC_STAFF, 'Academic Team'),
        (ADMIN_STAFF, 'Code Administration Team'),
        (ALUMNI, 'Alumni'),
        (EXTERNAL, 'External')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=32, null=True, blank=True, choices=OCCUPATION_CHOICES, default=STUDENT)
    institution = models.CharField(max_length=32, null=True, blank=True, choices=INSTITUTION_CHOICES, default=CODE)
    avatar = models.ImageField(upload_to='profile_images', null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    # TO DO PROVIDE PROFILECHANGEFORM FOR ADMIN 
    # def __str__(self):
    #     return  self.user

class ProfileDepartment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    departments = models.ManyToManyField(Department)

    @classmethod
    def add_department(cls, profile, new_department):
        profile_department, created = cls.objects.get_or_create(
            profile=profile
        )
        profile_department.departments.add(new_department)

    @classmethod
    def remove_department(cls, profile, department):
        profile_department, created = cls.objects.get_or_create(
            profile=profile
        )
        profile_department.departments.remove(department)

    # def __str__(self):
    #     return  "%s %s" % (self.profile.user, self.departments)

####### Mixins ##########

# source:
# https://stackoverflow.com/questions/1355150/django-when-saving-how-can-you-check-if-a-field-has-changed

# class ModelDiffMixin(object):
#     """A model mixin that tracks model fields' values 
#     and whether  fields have been changed."""

#     def __init__(self, *args, **kwargs):
#         super(ModelDiffMixins, self).__init__(*args, **kwargs)
#         self.__initial = self.dict

#     @property
#     def diff(self):
#         d1 = self.__initial
#         d2 = self._dict
#         diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
#         return dict(diffs)

#     @property
#     def has_changed(self):
#         return bool(self.diff)

#     @property
#     def changed_fields(self):
#         return self.diff.keys()

#     def get_field_diff(self, field_name):
#         """
#         Returns a diff for field if it's changed and None otherwise.
#         """
#         return self.diff.get(field_name, None)

#     def save(self, *args, **kwargs):
#         """
#         Saves model and set initial state.
#         """
#         super(ModelDiffMixin, self).save(*args, **kwargs)
#         self.__initial = self._dict

#     @property
#     def _dict(self):
#         return model_to_dict(self, 
#             fields=[field.name for field in self._meta.fields])

# Trigger creation of corresponding user profile as soon as Django User object has been created.
def create_profile(sender, **kwargs):
    # use keyword argument
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])
        profile.save()
# connect User and user profile
post_save.connect(create_profile, sender=User)
