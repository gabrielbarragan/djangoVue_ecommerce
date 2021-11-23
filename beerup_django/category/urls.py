from django.conf.urls import url
from django.urls import path, include

from category import views

urlpatterns = [
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]