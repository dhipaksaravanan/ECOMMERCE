# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        db_table = 'addresses'



class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
       
        db_table = 'cart'


class CartItems(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
      
        db_table = 'cart_items'


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'categories'




class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        db_table = 'order_items'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    shipping_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        
        db_table = 'orders'


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, blank=True, null=True)
    payment_date = models.DateTimeField()
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
       
        db_table = 'payments'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.ImageField(
    upload_to='images/',
    blank=True,
    null=True
)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'products'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'users'
