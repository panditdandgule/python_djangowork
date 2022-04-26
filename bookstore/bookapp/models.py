from django.db import models


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=70)
    book_isbn = models.CharField(max_length=70)
    book_genre = models.CharField(max_length=20)
    book_type = models.CharField(max_length=20)
    book_publishyear = models.DateField(null=True)
    book_price = models.IntegerField()
    book_condition = models.CharField(max_length=30)


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    publisher_country = models.CharField(max_length=60)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    author_firstname = models.CharField(max_length=100)
    author_lastname = models.CharField(max_length=100)


class BooksInventory(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    stockcount = models.IntegerField()


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_firstname = models.CharField(max_length=70)
    customer_lastname = models.CharField(max_length=90)
    customer_emailaddress = models.EmailField
    customer_mobile = models.CharField(max_length=12)
    customer_country = models.CharField(max_length=80)
    customer_otherdetails = models.CharField(max_length=300)


class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    orders_date = models.DateField(null=True)
    orders_subtotal = models.IntegerField()
    orders_shipping = models.CharField(max_length=200)
    orders_total = models.IntegerField()


class OrderItem(models.Model):
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class BillDetails(models.Model):
    billdetails_id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
