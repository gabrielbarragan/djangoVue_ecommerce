from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


# Create your views here.

class CategoryDetail(APIView):
    '''view details from Category'''

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)