from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:cat_slug>/',views.store,name='product_buy_category'),
    path('<slug:cat_slug>/<slug:pro_slug>/',views.product_detail,name='product_detail'),
]