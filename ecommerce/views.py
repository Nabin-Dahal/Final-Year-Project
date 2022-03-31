from django.shortcuts import render
<<<<<<< HEAD
from store.models import Product,ReviewRating


def home(request): 
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    context = {
        'products': products,
        'reviews': reviews,
=======
from store.models import Product


def home(request): 
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
>>>>>>> 978fff8db3d91e2cd874a6282f16c26b8298916d
    }
    return render(request, 'home.html',context)
    
    
    