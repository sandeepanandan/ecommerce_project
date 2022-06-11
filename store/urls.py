
from unicodedata import name
from django import views
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static
from store.controller import authview,cart,wishlist,checkout,order

urlpatterns = [

    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.productview,name='productview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.itemview,name='itemview'),

    path('register/',authview.UserCreationView.as_view(),name='register'),
    path('login/',authview.userloginview,name='login'),
    path('logout/',authview.logoutview,name='logout'),

    path('add-to-cart',cart.addtocartview,name='addtocart'),
    path('cart',cart.viewcartview,name='cart'),
    path('updatecart',cart.updatecartview,name='updatecart'),
    path('delete-cart-item',cart.deletecartview,name='deletecartitem'),

    path('wishlist',wishlist.wishlistview,name='wishlist'),
    path('add-to-wishlist',wishlist.addtowishlistview,name='addtowishlist'),
    path('delete-wishlist-item',wishlist.deleteitemview,name='deletewishitem'),

    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),
    path('proceed-to-pay',checkout.razorpaycheck),

    path('orders',order.index,name= 'orders'),
    path('view-orders/<str:t_no>',order.vieworder,name= 'vieworder'),
    path('my-orders',checkout.orders,name='myorders')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
