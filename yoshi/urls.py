from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('' , views.home , name='home' ),
    path('yoshi/<str:book_id>' , views.detail , name="yoshi"),
    path('addbook/' , views.addbooks , name="addbooks"),
    path('delete/<str:pk>' , views.deletebook , name='deletebook')

]
