from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.models import *
import random
from django.contrib.auth.models import User


def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_key > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    single_cart_total = []
    for item in cartitems:
        single_total = item.product.selling_price * item.product_key
        single_cart_total.append(single_total)
        total_price += item.product.selling_price * item.product_key

    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems': cartitems, 'total_price': total_price, 'userprofile': userprofile,'single_total': single_cart_total}
    return render(request, 'store/checkout.html', context)


@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('firstName')
            currentuser.last_name = request.POST.get('lastName')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.address = request.POST.get('address')
            userprofile.country = request.POST.get('country')
            userprofile.state = request.POST.get('state')
            userprofile.pincode = request.POST.get('zip')
            userprofile.save()

        neworder = Order()
        neworder.fname = request.POST.get('firstName')
        neworder.lname = request.POST.get('lastName')
        neworder.user = request.user
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.country = request.POST.get('country')
        neworder.state = request.POST.get('state')
        neworder.pincode = request.POST.get('zip')

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')


        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_key
        neworder.toatal_price = cart_total_price
        trackno = 'ecom' + str(random.randint(1111, 9999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'ecom' + str(random.randint(1111, 9999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_key
            )

        # to reduce the product quantity from available stock
        orderproduct = product.objects.filter(id=item.product.id).first()
        orderproduct.quantity = orderproduct.quantity - item.product_key
        orderproduct.save()
        # to clea rusers cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, 'Your order has been placed successfully')
        paymode = request.POST.get('payment_mode')
        if (paymode =='Paid by Razorpay' or paymode =='Paid by Paypal'):
            return JsonResponse({'status':'Your order has been placed successfully'})


    return redirect('/')


@login_required(login_url='login')
def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_key
    return JsonResponse({'total_price': total_price})

def orders(request):
    return redirect('myorders')
