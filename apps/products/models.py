from __future__ import unicode_literals
from django.db import models


# Create your models here.
class ProductsManager(models.Manager):
	def creator(self, **kwargs):
		if not kwargs['name'] or not kwargs['price']:
			return (False, "You must include a Name and Price for each product you create!")
		else: 
			self.create(name=kwargs['name'], description=kwargs['description'], price=kwargs['price'])
			return (True, "Success! Product has been added.")
	def destroy(self, **kwargs):
		self.filter(id=kwargs['id']).delete()
		return True
	def updater(self, **kwargs):
		if not kwargs['name'] or not kwargs['price']:
			return (False, "You must include a Name and Price for each product you create!")
		else:
			product = self.get(id=kwargs['id'])
			product.name=kwargs['name'] 
			product.description=kwargs['description']
			product.price=kwargs['price']
			product.save()
			return (True, "Success! Product has been updated.")


class Products(models.Model):
	name = models.CharField(max_length=45, null=False)
	description = models.CharField(max_length=200, null=True)
	price = models.FloatField(max_length=11, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = ProductsManager()

