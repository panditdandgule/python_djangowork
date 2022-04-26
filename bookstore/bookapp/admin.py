from django.contrib import admin
from .models import Books,Publisher,Author,BooksInventory,Customers,Orders,OrderItem,Bill,BillDetails

# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['book_id','book_title','book_isbn','book_genre','book_type','book_publishyear','book_price','book_condition']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['publisher_id','publisher_country']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_id','author_firstname','author_lastname']

@admin.register(BooksInventory)
class BooksInventoryAdmin(admin.ModelAdmin):
    list_display = ['stockcount']

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customer_id','customer_firstname','customer_lastname','customer_emailaddress','customer_mobile','customer_country','customer_otherdetails']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['orders_date','orders_subtotal','orders_shipping','orders_total']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity','price']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['customer_id','added_on']

@admin.register(BillDetails)
class BillDetailsAdmin(admin.ModelAdmin):
    list_display = ['bill_id','book_id','qty','added_on']
#admin.site.register(Books)
#admin.site.register(Publisher)
#admin.site.register(Author)
#admin.site.register(BooksInventory)
#admin.site.register(Customers)
#admin.site.register(Orders)
#admin.site.register(OrderItem)
#admin.site.register(Bill)
#admin.site.register(BillDetails)