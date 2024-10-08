import uuid
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
# from /the_eh_toko/settings import
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    image = models.ImageField(blank=False, upload_to="./media/", null=False)