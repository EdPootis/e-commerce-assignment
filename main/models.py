import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)