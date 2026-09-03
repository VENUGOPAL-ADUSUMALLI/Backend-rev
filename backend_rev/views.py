from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import serailzers
from .models import Product
from rest_framework.response import Response

# Create your views here.
def product_view(request):
    products = Product.objects.all();
    return  render(
        request,
        "products.html",
        {"products": products}
    )
# class ProductView(APIView):
#     def get(self,request):
#         products = Product.objects.all()
#         serailizer = serailzers.ProductSerializer(products, many=True)
#         print(serailizer.data)
#         return Response(serailizer.data)
#     def post(self, request):
#         serailizer = serailzers.ProductSerializer(data=request.data)
#         if serailizer.is_valid():
#             serailizer.save()
#             print(serailizer.validated_data)
#             return Response(
#                 serailizer.data,
#                 status=201
#             )
#         return Response(
#             serailizer.errors,
#             status=400
#         )

class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serailzers.ProductSerializer

class ProductDetailedView(RetrieveUpdateDestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class =  serailzers.ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = serailzers.ProductSerializer
    def get_queryset(self) :
        return Product.objects.filter(
            is_available= True
        )
    @action(detail=True, methods=["POST"], url_path="mark-unavailable")
    def mark_unavailable(self, request, pk=None):
        product = self.get_object()
        product.is_available = False
        product.save()
        return  Response({
            "message": "Product marked as unavailable"
        })


