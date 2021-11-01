from django.conf.urls import url
from django.urls import path, include

from product import views

urlpatterns = [
    path('lastest-products/', views.LastestProductsList.as_view()),
]