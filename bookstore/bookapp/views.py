from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Books, Publisher, Author, BooksInventory, Customers, Orders, OrderItem, Bill, BillDetails
from .serializers import BooksSerializer, PublisherSerializer, AuthorSerializer, BookInventorySerializer, \
    CustomersSerializer, OrdersSerializer, OrderItemSerializer, BillSerializer, BillDetailsSerializer, \
    OrderItemSerializerSimple


# Create your views here.
class BooksViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Books List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = BooksSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'Books Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving books data"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Books.objects.all()
            book = get_object_or_404(queryset, pk=pk)
            serializer = BooksSerializer(book, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'Successfully Updated Books Data'}
        except:
            dict_response
            {"error": False, 'message': "Error During Updating Books data"}
        return Response(dict_response)


class PublisherViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = PublisherSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'Publisher Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving Publisher data"}
        return Response(dict_response)

    def list(self, request):
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Books List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, pk=pk)
        serializer = PublisherSerializer(publisher, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, pk=pk)
        serializer = PublisherSerializer(publisher, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data has been updated"})


class AuthorViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = AuthorSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'Author Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving Author data"}
        return Response(dict_response)

    def list(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All author List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data has been updated"})


class BookInventoryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = BookInventorySerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'BookInventory Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving BookInventory data"}
        return Response(dict_response)

    def list(self, request):
        booksinventory = BooksInventory.objects.all()
        serializer = BookInventorySerializer(booksinventory, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All BooksInventory List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = BooksInventory.objects.all()
        booksinventory = get_object_or_404(queryset, pk=pk)
        serializer = BookInventorySerializer(booksinventory, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = BooksInventory.objects.all()
        booksinventory = get_object_or_404(queryset, pk=pk)
        serializer = PublisherSerializer(booksinventory, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data has been updated"})


class CustomersViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CustomersSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'Customers Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving Customer data"}
        return Response(dict_response)

    def list(self, request):
        customer = Customers.objects.all()
        serializer = CustomersSerializer(customer, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All customer List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Customers.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomersSerializer(customer, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Customers.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomersSerializer(customer, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data has been updated"})


'''
class OrdersViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = OrdersSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {'error': False, 'message': 'Orders Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving Orders data"}
        return Response(dict_response)

    def list(self, request):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All orders List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Orders.objects.all()
        orders = get_object_or_404(queryset, pk=pk)
        serializer = OrdersSerializer(orders, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Orders.objects.all()
        orders = get_object_or_404(queryset, pk=pk)
        serializer = OrdersSerializer(orders, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data has been updated"})
'''


class OrdersViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = OrdersSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Access the serializer id which JUST save in our database table
            orders_id = serializer.data['orders_id']
            # print(order_id)

            # Adding and Saving Id into Order Details Table
            orders_details_list = []
            for order_detail in request.data["OrderItem"]:
                print(order_detail)

                # Adding order id which will work for order details serializer
                order_detail["orders_id"] = orders_id
                orders_details_list.append(order_detail)
                print(order_detail)

            serializer2 = OrderItemSerializer(data=orders_details_list, many=True, context={"request": request})
            serializer2.is_valid()
            serializer2.save()

            dict_response = {'error': False, 'message': 'Orders Data Save Successfully'}
        except:
            dict_response
            {"error": False, 'message': "Error During Saving Orders data"}
        return Response(dict_response)

    def list(self, request):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True, context={'request': request})

        orders_deta = serializer.data
        neworderlist = []

        # Adding Extra key for Orders Details in Orders
        for order in orders_deta:
            # Accessing all the orders details of Current Orders ID
            order_details = OrderItem.objects.filter(orders_id=orders["orders_id"])
            order_details_serializer = OrderItemSerializerSimple(order_details, many=True)
            order["order_details"] = order_details_serializer.data
            neworderlist.append(order)

        response_dict = {'error': False, 'message': 'All Orders list Data', 'data': neworderlist}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Orders.objects.all()
        orders = get_object_or_404(queryset, pk=pk)
        serializer = OrdersSerializer(orders, context={"request": request})

        serializer_data = serializer.data

        # Accessing all the orders details of Current orders ID
        order_details = OrderItem.objects.filter(orders_id=serializer_data["orders_id"])
        order_details_serializer = OrderItemSerializerSimple(order_details, many=True)
        serializer_data["order_details"] = order_details_serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        queryset = Orders.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrdersSerializer(order, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data has been updated"})


book_list = BooksViewSet.as_view({"get": "list"})
book_create = BooksViewSet.as_view({"post": "create"})
book_update = BooksViewSet.as_view({"put": "update"})
