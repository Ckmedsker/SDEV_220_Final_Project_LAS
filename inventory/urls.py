from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name='dashboard_page'), #root 'landing page/home page'
    path('products/', views.products_page, name='products_page'),
    path('sales/', views.sales_page, name='sales_page'),
    path('inventory/', views.inventory_page, name='inventory_page'),

    # these are example templates to help remember what is going on
    # otherPageView1 and the other two are linked to views.py, the names must be changed together
    
    #path('/inventory/', views.otherPageView1, name='otherpageVAR1'),
    #path('/sales/', views.otherPageView2, name='otherpageVAR2'),
    #path('/etc/', views.otherPageView3, name='otherpageVAR3'),
] 