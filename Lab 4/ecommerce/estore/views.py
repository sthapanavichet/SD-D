from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Cart, CartItem, Order
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("Your Estore application is working")

def checkout(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    order = Order.objects.create(
        user = user,
        total_price = sum(item.product.price * item.quantity for item in cart.cartitem_set.all()),
        shipping_address = '',
    )
    order.items.add(*cart.cartitem_set.all())

    for cartitem in cart.cartitem_set.all():
        product = cartitem.product
        product.stock -= cartitem.quantity
        product.save()

    order.save()
    cart.delete()
    return render(request, 'checkout.html')


def view_cart(request):
    user = request.user
    cart, cart_created = Cart.objects.get_or_create(user=user)

    total = sum(item.product.price * item.quantity for item in cart.cartitem_set.all())

    context = {
        'cart_items': cart.cartitem_set.all(),
        'total': total,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    ret = False
    if request.method == 'POST':
        user = request.user
        product = Product.objects.get(id = product_id)
        quantity = request.POST.get('quantity')

        cart, cart_created = Cart.objects.get_or_create(user = user)
        cartitem, cartitem_created = CartItem.objects.get_or_create(cart = cart, product = product, defaults={'quantity': quantity})

        if not cartitem_created:
            cartitem.quantity += quantity

        cartitem.save()
        cart.save()
        ret = True
    return JsonResponse({'success': ret, 'quantity' : quantity})



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
