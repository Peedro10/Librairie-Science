from django.db import models
from store.models import Book
from django.contrib.auth.models import User

from datetime import date
from django import forms




class Order(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	nom = models.CharField(max_length=30)
	email = models.EmailField()
	Telphone = models.CharField(max_length=16)
	address = models.CharField(max_length=150)
	region = models.CharField(max_length=20)
	ville = models.CharField(max_length=30)
	zip_code = models.CharField(max_length=30)
	payment_method = models.CharField(max_length = 20)
	N_compte= models.CharField(max_length = 20)
	transaction_id = models.IntegerField()
	payable = models.IntegerField()
	totalbook = models.IntegerField()
	created = models.DateField(auto_now_add=True)
	date_return = models.DateField(null=True, blank=True)
 
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	chekbook = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created','date_return' )

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())





class Caisse(models.Model):
	date=models.DateField(auto_now=False,auto_created=False,auto_now_add=False,null=True,blank=True)
	checkout_day = models.DecimalField(max_digits=10, decimal_places=2,null=True)

	# def caisse():
	# 	total_cost = sum(order.get_total_cost() for order in Order.objects.filter(paid=True))
	# 	caisse = Caisse.objects.create(date=date.today(), caisse_jour=total_cost)
	# 	caisse.save()
	# 	return caisse


	def __str__(self):
		return 'Caisse {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price




