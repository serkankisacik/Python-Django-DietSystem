from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting
from program.models import Category, Program
from randevu.models import RandevuForm, Randevu, OrderForm, Order
from user.models import UserProfile


def index(request):
    return HttpResponse("Randevu Page")



@login_required(login_url="/login")
def randevual(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = RandevuForm(request.POST)
        if form.is_valid():
            data = Randevu()  # create relation with model
            data.date = form.cleaned_data['date']
            data.time = form.cleaned_data['time']
            data.yas = form.cleaned_data['yas']
            data.kilo = form.cleaned_data['kilo']
            data.boy = form.cleaned_data['boy']
            data.ip = request.META.get('REMOTE_ADDR')
            data.program_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table
            messages.success(request, "Randevunuz Alınmıştır. Ödemeyi Yaptıktan Sonra Size Dönüş Yapılacaktır. Teşekkür ederiz.")
            return HttpResponseRedirect("/user/randevu")

    return HttpResponseRedirect(url)




def order(request,id):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':  # check post
       lasturl=request.META.get('HTTP_REFERER')
       form = OrderForm(request.POST)
       if form.is_valid():
            data = Order()  # create relation with model
            data.randevu_id = id
            data.first_name = form.cleaned_data['first_name']  # get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Ödeme Yapılmıştır! Diyet Programına Erişmek İçin Yönetici Onayı Gerekiyor! Lütfen Bekleyiniz.')
            return HttpResponseRedirect("/user/orders")
       else:
            messages.warning(request, ' form error :' + str(form.errors))
            return HttpResponseRedirect(lasturl)

    else:
        randevu = Randevu.objects.get(id=id)
        orders = Order.objects.filter(randevu_id=id)
        form= OrderForm()


        context = {
            'randevu': randevu,
            'orders': orders,
            'form': form,
            'category':category,
            'setting':setting,
            'profile':profile
        }
        return render(request, 'order_form.html', context)


def content(request,id):
    randevu = Randevu.objects.get(id=id)
    order = Order.objects.filter(randevu_id=id)
    context = {
        'randevu': randevu,
        'order': order,

    }
    return render(request, 'content_order.html', context)