from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework	import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response



# class ListCategory(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductFilter(generics.ListAPIView):
# 	queryset=Product.objects.all()
# 	serializer_class=ProductSerializer
# 	permission_classes=(AllowAny,)
# 	filter_backends=[filters.SearchFilter]
# 	search_fields=['category', 'name']


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# @api_view(['GET', 'POST'])
# def product_list(request):

# 	if request.method == 'GET':
# 		products = Product.objects.all()
# 		serializer = ProductSerializer(products, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = ProductSerializer(data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)

# 		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
# 	try:
# 		product = Product.objects.get(pk=pk)
# 	except Product.DoesNotExist:
# 		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = ProductSerializer(product)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = ProductSerializer(data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		product.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def recent_added(request):
	products = Product.objects.order_by('-date_created')[0:2]
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def best_offer(request):
	products = Product.objects.order_by('price')[0:2]
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)

class ProductFilter(generics.ListAPIView):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer
	permission_classes=(AllowAny,)
	filter_backends=[filters.SearchFilter]
	search_fields=['category', 'name']