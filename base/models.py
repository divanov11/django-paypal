from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	image_url = models.CharField(max_length=1000, null=True, blank=True)
	price = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.name
