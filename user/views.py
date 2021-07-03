from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting
from program.models import Category, Program, Comment
from randevu.models import Randevu, Order
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile
# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context={
        'setting':setting,
        'category':category,
        'profile':profile,

             }
    return render(request,'user_profile.html',context)


@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'setting': setting,
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login') # Check login
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form,'category': category,'setting':setting,
                       })


@login_required(login_url="/login")
def randevu(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    randevu = Randevu.objects.filter(user_id=current_user.id)
    order = Order.objects.filter(user_id=current_user.id)

    context = {
        'category': category,
        'randevu': randevu,
        'setting': setting,
        'order':order
    }
    return render(request, 'user_randevu.html', context)

@login_required(login_url="/login")
def orders(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)

    context = {
        'category': category,
        'randevu': randevu,
        'setting': setting,
        'orders':orders,
    }
    return render(request, 'user_orders.html', context)

@login_required(login_url="/login")
def randevudelete(request,id):
    current_user = request.user
    Randevu.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request,'Rezervasyon İptal Edildi')
    return HttpResponseRedirect('/user/randevu')


@login_required(login_url="/login")
def comments(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)

    context = {
        'category': category,
        'comment': comment,
        'setting': setting,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url="/login")
def commentdelete(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request,'Yorum Silindi!')
    return HttpResponseRedirect('/user/comments')


