from django.contrib import admin

from profiles.models import Profile
from videos.models import Job, Series


admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Series)
