from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages


# Create your views here.
def cart_info(user):
    usera = user
    cart = Cart.objects.filter(user=usera)
    total_qty = 0
    for qty in cart:
        total_qty= total_qty+qty.product_key
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_key
    
    cart_details = [total_qty,total_price]
    
    return cart_details

def home(request):
    top_selling = product.objects.filter(trending=1)
    trending_products = product.objects.filter(trending=1)
    collections = category.objects.filter(status=0)
    user = request.user
    cart_details = cart_info(user)
    context = {'category': collections,'topnew':trending_products,'topsell':top_selling,'qty':cart_details[0],'price':cart_details[1]}
    return render(request, 'index.html', context)

def collections(request):
    user = request.user
    cart_details = cart_info(user)

    collections = category.objects.filter(status=0)
    context = {'category': collections,'qty':cart_details[0],'price':cart_details[1]}

    return render(request, 'store/category.html', context)


def productview(request, slug):
    user = request.user
    cart_details = cart_info(user)

    if (category.objects.filter(slug=slug, status=0)):
        products = product.objects.filter(category__slug=slug)
        category_name = category.objects.filter(slug=slug).first()
        context = {'products': products, 'name': category_name,'qty':cart_details[0],'price':cart_details[1]}
        return render(request, 'store/shop.html', context)
    else:
        messages.warning(request, 'no such category found')
        return redirect('home')


def itemview(request, cate_slug, prod_slug):
    user = request.user
    cart_details = cart_info(user)
    
    if (category.objects.filter(slug=cate_slug, status=0)):
        all_products = product.objects.filter(category__slug=cate_slug)
        if (product.objects.filter(slug=prod_slug, status=0)):
            products = product.objects.filter(slug=prod_slug, status=0).first()
            n = ['abcd']
            context = {'product': products, 'all': all_products, 'n': n,'qty':cart_details[0],'price':cart_details[1]}


        else:
            messages.warning(request, 'no such product foundd')
            return redirect('collections')
    else:
        messages.warning(request, 'no such category foundd')
        return redirect('collections')
    return render(request, 'store/products/single-product.html', context)

