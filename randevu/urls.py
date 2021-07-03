from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randevual/<int:id>', views.randevual, name='randevual'),
    path('order/<int:id>', views.order, name='order'),
    path('content/<int:id>', views.content, name='content'),

]