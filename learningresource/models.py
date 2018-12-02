from django.db import models
from accounts.models import Department, User, Profile

class MediaType(models.Model):
    media_type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.media_type_name

class Tag(models.Model):
    tag_name = models.CharField(max_length = 40)

    def __str__(self):
        return self.tag_name

class Module(models.Model):
    module_name = models.CharField(db_index=True, max_length=255)

    def __str__(self):
        return self.module_name

class LearningResource(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=600)
    description = models.TextField()
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, db_index=True, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    last_edit_date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=255, default='other')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def short_title(self):
        return '{}...'.format(self.title[:50])

class LearningResourceTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    learningresource = models.ForeignKey(LearningResource, on_delete=models.CASCADE)

class ProfileLearningResource(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    learningresource = models.ForeignKey(LearningResource, on_delete=models.CASCADE)

class LearningResourceModule(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    learningresource = models.ForeignKey(LearningResource, on_delete=models.CASCADE)
