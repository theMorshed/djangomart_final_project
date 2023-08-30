from django.urls import path
from store.views import store, product_details

urlpatterns = [
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_details, name='product_details'),
]
