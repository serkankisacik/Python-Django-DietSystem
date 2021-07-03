from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import  SignUpForm
from home.models import Setting, ContactFormMessage, FAQ, ContactForm
from program.models import *
from user.models import UserProfile


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Program.objects.all().order_by('?')[:4]
    lastprograms = Program.objects.all().order_by('-id')[:6]
    randomprograms = Program.objects.all().order_by('?')[:3]
    sporprograms = Program.objects.filter(category='1').order_by('?')[:3]
    kisiprograms = Program.objects.filter(category='2').order_by('?')[:3]
    hastalikprograms = Program.objects.filter(category='3').order_by('?')[:3]
    yasprograms = Program.objects.filter(category='4').order_by('?')[:3]
    category = Category.objects.all()

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'lastprograms': lastprograms,
               'randomprograms': randomprograms,
               'sporprograms': sporprograms,
               'kisiprograms': kisiprograms,
               'hastalikprograms': hastalikprograms,
               'yasprograms': yasprograms,


               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'hakkimizda', 'category': category}
    return render(request, 'hakkimizda.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'referans', 'category': category}
    return render(request, 'references.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarılı ile gönderilmiştir. Teşekkür Ederiz ")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)


def category_programs(request,id,slug):
    programs = Program.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)

    context = {'programs':programs,
               'category':category,
               'slug':slug,
               'setting': setting,
               'categorydata':categorydata,

               }
    return render(request,'programs.html',context)



def program_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    image = Images.objects.filter(program_id=id)
    program = Program.objects.get(pk=id)
    comments = Comment.objects.filter(program_id=id,status='True')
    context = {
        'program': program,
        'category': category,
        'image': image,
        'comments': comments,
        'setting': setting,
    }
    return render(request, 'program_detail.html', context)





def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş başarısız. Tekrar Deneyiniz.")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'form':form,
        'setting': setting,
    }
    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    faq = FAQ.objects.all()
    context = {'category': category,
               'faq': faq,
               'setting':setting,
               }
    return render(request, 'faq.html', context)


