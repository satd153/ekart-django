from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.
def store(request,cat_slug=None):
    products=None
    categories=None
    pro_count=None
    if(cat_slug!=None):
        categories=get_object_or_404(Category,slug=cat_slug)
        products= Product.objects.all().filter(category=categories,is_avl=True)
        pro_count=products.count()
    else:
        products= Product.objects.all().filter(is_avl=True)
        pro_count=products.count()
    context ={
        "products":products,
        "count":pro_count,
    }
    return render(request,'store/store.html',context)

def product_detail(request,cat_slug,pro_slug):
    try:
        product=products= Product.objects.get(category__slug=cat_slug,slug=pro_slug)
    except Exception as e:
        raise e
    return render(request,'store/product_detail.html',{'product':product})
