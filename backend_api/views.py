from django.shortcuts import render
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.response import Response


class ProductsView(APIView):
    def get(self, request):
        output = [
            {
                'title': output.title,
                'description': output.description
            } for output in Products.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)