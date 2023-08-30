from django.urls import path
from cart.views import cart, add_to_cart, remove_from_cart, remove_cart_item

urlpatterns = [
    path('', cart, name='cart'),
    path('<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('remove_item/<int:product_id>/', remove_cart_item, name='remove_cart_item'),
]
