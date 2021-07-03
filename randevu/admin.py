from django.contrib import admin

# Register your models here.
from randevu.models import Randevu, Order


class RandevuAdmin(admin.ModelAdmin):
    list_display = ['program','date','time','yas','kilo','boy','status','create_at','user']
    list_filter = ['status']
    readonly_fields = ('date','time','user','program','id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','last_name','ip','randevu')
    can_delete = False

admin.site.register(Randevu,RandevuAdmin)
admin.site.register(Order,OrderAdmin)