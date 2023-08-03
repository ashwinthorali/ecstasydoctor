from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('apply', views.apply, name='apply'),
    path('merchant-cash-advance/', views.mca, name='mca'),
    path('credit-card-processing/', views.ccp, name='ccp'),
    path('industries/', views.industry, name='industry'),
    path('blogs/', views.blogs, name='blogs'),
    path('referral-program-merchant-cash-advance/', views.referral, name='referral'),
    path('referral-program-terms-conditions/', views.referral_td, name='referral_td'),
    path('terms-and-conditions/', views.term, name='term'),
    path('privacy-policy/', views.privacy, name='privacy'),
    
    #new changes
    path('careers/', views.careers, name='careers'),
    path('careers/<str:pk>/', views.careers_detail, name='careers_detail'),
    path('blogs/<str:pk>/', views.blogs_detail, name='blogs_detail'),
   
] 
