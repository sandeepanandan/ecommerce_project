from django.http import JsonResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from store.models import product,Cart
from django.contrib.auth.decorators import login_required


def addtocartview(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id")) 
            product_check = product.objects.get(id=prod_id)
            if (product_check):
                if (Cart.objects.filter(user=request.user.id,product_id = prod_id)):
                    return JsonResponse({'status':'Product Already in Cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id = prod_id,product_key= prod_qty)
                        return JsonResponse({'status':'Product Added succesfully'})
                    else:
                        return JsonResponse({'status':'Only' + str(product_check.quantity)+ 'quantity available'})                              
            else:
                return JsonResponse({'status':'No Such product find'})
        else:
            context = {'status':"Login to Continue"}
            return JsonResponse(context)
    return redirect('/')

@login_required(login_url='login')
def viewcartview(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render (request,'store/cart.html',context)


def updatecartview(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user,product_id = prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id,user= request.user) 
            cart.product_key = prod_qty          
            cart.save()
            return JsonResponse({'status':'updated successfully'})

    return redirect('/')

def deletecartview(request):
    if request.method =='POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user= request.user,product_id = prod_id)):
            cartitem = Cart.objects.get(user= request.user,product_id = prod_id)
            cartitem.delete()
        return JsonResponse({'status':'deleted successfully'})
    return redirect('/')
            