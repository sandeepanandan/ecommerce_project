from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.http import JsonResponse

from store.models import Cart, Wishlist, product
@login_required(login_url='login')
def wishlistview(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render (request,'store/wishlist.html',context)


def addtowishlistview(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = product.objects.get(id = prod_id)
            if product_check:
                if (Wishlist.objects.filter(user=request.user,product_id = prod_id)):
                    return JsonResponse({'status':"Item is Already in wishlist"})
                else:
                    Wishlist.objects.create(user = request.user,product_id = prod_id)
                    return JsonResponse ({'status':"Item Is Added To Wishlist"})
            return JsonResponse({'status':'No Such product find'})
        return redirect('login')
    return redirect('/')

def deleteitemview(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if  (Wishlist.objects.filter(user= request.user,product_id = prod_id)):
                wishlist = Wishlist.objects.get(product_id = prod_id)
                wishlist.delete()
            return JsonResponse ({'status':'No Such product find'})
        return redirect('login')    

    return redirect('/')