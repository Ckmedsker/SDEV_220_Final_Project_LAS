from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'), #root 'landing page/home page'

    # these are example templates to help remember what is going on
    # otherPageView1 and the other two are linked to views.py, the names must be changed together
    
    #path('/inventory/', views.otherPageView1, name='otherpageVAR1'),
    #path('/sales/', views.otherPageView2, name='otherpageVAR2'),
    #path('/etc/', views.otherPageView3, name='otherpageVAR3'),
] 