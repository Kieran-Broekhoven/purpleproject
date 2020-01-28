from django.urls import path, re_path

from api import views

urlpatterns = [
    path('sendMail/', views.sendMail),
    path('wishlist/', views.wishlist),
]
