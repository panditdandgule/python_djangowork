from django.shortcuts import render
from .models import Product

# Create your views here.
def welcome_page(request):
    return render(request,'products/welcome.html')

def save_products(request):
    if request.method=='POST':
        formdata=request.POST
        pid=formdata.get('id')
        products=None
        if pid:
            products=Product.objects.filter(id=pid).first()
        if products:
            products.name=formdata['name']
            products.price=formdata['price']
            products.vendor=formdata['vendor']
            products.save()
            products=Product.objects.filter(is_active=True).all()
            return render(request,'products/show.html',{'products':products})
        else:
            products=Product(
                name=formdata['name'],
                price=formdata['price'],
                vendor=formdata['vendor']
            )
            products.save()
            products=Product.objects.filter(is_active=True).all()
            return render(request,'products/show.html',{'products':products})

    return render(request,'products/add.html')

def list_products(request):
    products=Product.objects.filter(is_active=True).all()
    return render(request,'products/show.html',{'products':products})

def delete_product(request,pid):
    product=Product.objects.filter(id=pid).first()
    if product:
        product.is_active=False
        product.save()
        products=Product.objects.filter(is_active=True).all()
        return render(request,'products/show.html',{'products':products})