from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Product
from django.utils import timezone
def home(request):
    return render(request, 'products/home.html')
@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.tile=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startwidth('http://') or request.POST['url'].startwidth('https//'):
                product.url=request.POST['url']
            else:
                product.url='htttp://' + request.POST['url']
            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.hunter=request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/create.html', {'error':'All fields required'})
    else:
        return render(request, 'products/create.html')
