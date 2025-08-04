from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=8)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    subtotal = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, related_name="items" ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class LoyaltyPointLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    point_added = models.IntegerField()
    reason = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)