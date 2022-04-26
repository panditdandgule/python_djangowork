from rest_framework import serializers
from .models import Books, Publisher, Author, BooksInventory, Customers, Orders, OrderItem, Bill, BillDetails


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

    '''Overriding method here'''

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['books'] = BooksSerializer(instance.book_id).data
        return response


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def to_representation(self, instance):
        response = super(AuthorSerializer, self).to_representation(instance)
        response['books'] = BooksSerializer(instance.book_id).data
        return response


class BookInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksInventory
        fields = "__all__"

    def to_representation(self, instance):
        response = super(BookInventorySerializer, self).to_representation(instance)
        response['books'] = BooksSerializer(instance.book_id).data
        return response


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

    def to_representation(self, instance):
        response = super(OrdersSerializer, self).to_representation(instance)
        response['customers'] = CustomersSerializer(instance.customer).data
        return response


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def to_representation(self, instance):
        response = super(OrderItemSerializer, self).to_representation(instance)
        response['books'] = BooksSerializer(instance.book_id).data
        return response

class OrderItemSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomersSerializer(instance.customer_id).data
        return response


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['books'] = BooksSerializer(instance.book_id).data
        return response
