from django.shortcuts import render

def landing_page(request):
    return render(request, 'inventory/index.html', {}) #the directory inventory/index.html is grabbing is in the templates folder in the project

def products_page(request):
    return render(request, 'inventory/products.html', {})

def sales_page(request):
    return render(request, 'inventory/sales.html', {})

def dashboard_page(request):
    return render(request, 'inventory/dashboard.html', {})

# these are example templates to help remember what is going on
# otherPageView1 and the other two are linked to urls.py, the names must be changed together

# def otherPageView1(request):          
#     return render(request, 'inventory/page.html', {})

# def otherPageView2(request):
#     return render(request, 'inventory/otherPage.html', {})

# def otherPageView3(request):
#     return render(request, 'inventory/yetAnotherPage.html', {})
