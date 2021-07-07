from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Orderserializer

# Create your views here.
class OrderView(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = Orderserializer
	def post(self, request, id, format=None):
		serializer=self.serializer_class(data=request.data)
		user=request.user
		if serializer.is_valid():
			try:
					qs_objects=Product.objects.get(id=1)
					Leesee=Product.Leesee
					order_quantity=serializer.data['Quantity']
					Date_of_order=serializer.data['Date_of_order']
					Date_of_return=serializer.data['Date_of_return']
					Delivery=serializer.data['Delivery']
					Time_of_order=serializer.data['Time_of_order']
					current_quantity=qs_objects.quantity
					if order_quantity > current_quantity:
						content={'Error': "Order exceeds that in stock"}
						return Response(content, status=status.HTTP_400_BAD_REQUEST)

					else:


						new_product_quantity=current_quantity-order_quantity

					if new_product_quantity==0:

						qs_objects.status=False

					qs_objects.quantity=new_product_quantity
					qs_objects.Customer=user
					qs_objects.Date_of_order=Date_of_order
					qs_objects.Date_of_return=Date_of_return
					qs_objects.Delivery=Delivery
					qs_objects.Time_of_order=Time_of_order



					qs_objects.save()
					content={'Quantity':order_quantity,
					'Product':qs_objects,
					'Remaining in stock':new_product_quantity,
					Date_of_order:Date_of_order,
					Date_of_return:Date_of_return,
					'Vendor': Leesee
					'Delivery method'=Delivery
					}
					return Response(content, status=status.HTTP_201_CREATED)
			except:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		



						