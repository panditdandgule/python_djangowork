# Generated by Django 3.1.7 on 2021-12-15 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=70)),
                ('book_isbn', models.CharField(max_length=70)),
                ('book_genre', models.CharField(max_length=20)),
                ('book_type', models.CharField(max_length=20)),
                ('book_price', models.IntegerField()),
                ('book_condition', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_firstname', models.CharField(max_length=70)),
                ('customer_lastname', models.CharField(max_length=90)),
                ('customer_mobile', models.CharField(max_length=12)),
                ('customer_country', models.CharField(max_length=80)),
                ('customer_otherdetails', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.AutoField(primary_key=True, serialize=False)),
                ('publisher_country', models.CharField(max_length=60)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.books')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orders_id', models.AutoField(primary_key=True, serialize=False)),
                ('orders_subtotal', models.IntegerField()),
                ('orders_shipping', models.CharField(max_length=200)),
                ('orders_total', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.customers')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.books')),
                ('orders_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.orders')),
            ],
        ),
        migrations.CreateModel(
            name='BooksInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockcount', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.books')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('billdetails_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.bill')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.books')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.customers'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_firstname', models.CharField(max_length=100)),
                ('author_lastname', models.CharField(max_length=100)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.books')),
            ],
        ),
    ]
