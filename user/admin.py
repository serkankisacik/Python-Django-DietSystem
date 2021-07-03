from django.contrib import admin

# Register your models here.
from user.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','image_tag','phone','city']



admin.site.register(UserProfile,UserProfileAdmin)