from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.
def store(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category)
        page_number = request.GET.get('page')
        paginator = Paginator(products, 1)
        paged_product = paginator.get_page(page_number)
    else:
        products = Product.objects.filter(is_available=True)
        page_number = request.GET.get('page')
        paginator = Paginator(products, 3)
        paged_product = paginator.get_page(page_number)
        
    categories = Category.objects.all()
    context = {
        'products': paged_product,
        'categories': categories
    }
    return render(request, 'store/store.html', context)
