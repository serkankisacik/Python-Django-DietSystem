from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, FAQ


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','note','status']
    list_filter = ['status']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','status']
    list_filter = ['status']






admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(FAQ,FAQAdmin)
