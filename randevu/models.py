from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from program.models import Program

class Randevu(models.Model):
    STATUS = (
        ('Odeme Yapildi', 'Odeme Yapildi'),
        ('Odeme Yapilmadi', 'Odeme Yapilmadi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    yas = models.IntegerField(default=1)
    kilo = models.IntegerField(default=1)
    boy = models.IntegerField(default=1)
    status=models.CharField(max_length=20,choices=STATUS, default='Odeme Yapilmadi')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)



class RandevuForm(ModelForm):

    class Meta:
        model = Randevu
        fields = ['date','time','yas','kilo','boy']

    def __str__(self):
        return self.program.title



class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    randevu = models.ForeignKey(Randevu, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    diyetisyennotu = RichTextUploadingField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.user.first_name

    def __str__(self):
        return self.randevu.program.title


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','address','phone','city','country']





