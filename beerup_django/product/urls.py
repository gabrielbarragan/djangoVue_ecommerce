from django.conf.urls import url
from django.urls import path, include

from product import views

urlpatterns = [
    path('lastest-products/', views.LastestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view())
]