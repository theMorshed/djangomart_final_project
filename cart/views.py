from django.shortcuts import render, redirect
from store.models import Product
from cart.models import Cart, CartItem

# Create your views here.
def cart(request):
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id=session_id)
    cart_id = Cart.objects.filter(cart_id=session_id).exists()
    cart_items = None
    total = 0
    tax = 0
    grand_total = 0
    if cart_id:
        cart_items = CartItem.objects.filter(cart = cartid)
        for item in cart_items:
            total += item.sub_total()
    tax = (total * 2) / 100
    grand_total = total + tax
    context = {'cart_items': cart_items, 'total': total, 'tax': tax, 'grand_total': grand_total}
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.session.session_key:
        request.session.create()
        
    session_id = request.session.session_key
    cart_id = Cart.objects.filter(cart_id=session_id).exists()
    if cart_id:
        cart_item = CartItem.objects.filter(product=product).exists()
        if cart_item:
            item = CartItem.objects.get(product=product)
            item.quantity += 1
            item.save()
        else:
            cart_id = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
                product = product,
                cart = cart_id,
                quantity = 1
            )
            item.save()
    else:
        cart_id = Cart.objects.create(
            cart_id = session_id
        )
        cart_id.save()
    
    return redirect('cart')

def remove_from_cart(request, product_id):
    session_id = request.session.session_key
    product = Product.objects.get(id = product_id)
    cart = Cart.objects.get(cart_id = session_id)
    cart_item = CartItem.objects.get(cart = cart, product = product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
        
    return redirect('cart')

def remove_cart_item(request, product_id):
    session_id = request.session.session_key
    product = Product.objects.get(id = product_id)
    cart = Cart.objects.get(cart_id = session_id)
    cart_item = CartItem.objects.get(cart = cart, product = product)
    cart_item.delete()
    return redirect('cart')