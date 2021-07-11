from django.contrib import admin

from .models        import Profile, ProfileStatus

admin.site.register(Profile)
admin.site.register(ProfileStatus)