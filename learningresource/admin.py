from django.contrib import admin
from .models import MediaType, Tag, LearningResource, LearningResourceTag, ProfileLearningResource

admin.site.register(MediaType)
admin.site.register(Tag)
admin.site.register(LearningResource)
admin.site.register(LearningResourceTag)
admin.site.register(ProfileLearningResource)
