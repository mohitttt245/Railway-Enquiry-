from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# from .views import ordered_products

#URL conf
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.homepage , name='homepage'),
    path('user/',views.user_page , name='user-page' ),
    path('About_us/',views.about, name = 'About-us'),
    path('contact/', views.contact_us, name='contact'),
    path('trainuser/',views.trainuser, name='trainuser'),
    path('train_shedule/',views.train_shedule, name="train_shedule"),
    path('saveenquiry/',views.booking, name='saveenquiry'),
    path('payment/',views.payment,name='payment'),
    path('booking/',views.booking, name='booking'),
    path('successfull/',views.success, name='successfull'),
]