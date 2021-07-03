from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from program.models import CommentForm, Comment


def index(request):
    return HttpResponse("Program Page")


def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.ip = request.META.get('REMOTE_ADDR')
         data.program_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Yorumunuz Gönderilmiştir. Teşekkür ederiz.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)
