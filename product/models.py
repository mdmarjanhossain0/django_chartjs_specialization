from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")