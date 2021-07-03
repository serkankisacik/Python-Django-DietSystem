from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('randevu/', views.randevu, name='randevu'),
    path('orders/', views.orders, name='orders'),
    path('randevudelete/<int:id>', views.randevudelete, name='randevudelete'),
    path('comments/', views.comments, name='comments'),
    path('commentdelete/<int:id>', views.commentdelete, name='commentdelete'),
]