from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class RegUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

class UserCache(models.Model):
    phone_no = models.IntegerField()

class Category(models.Model):
    categoryId = models.IntegerField(primary_key=True)
    categoryName = models.CharField(unique=True, max_length=255)
    categoryImagePath = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.categoryName


class CategorizedProducts(models.Model):
    under_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    product_name = models.CharField(unique=True, max_length=255)
    product_id = models.IntegerField(primary_key=True)
    product_price = models.IntegerField()
    product_rating = models.FloatField()
    product_descp = models.CharField(max_length=255)
    product_imagepath = models.CharField(max_length=255, default='media/images/clothing.png')

    def __str__(self):
        return self.product_name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')


class Addresses2(models.Model):
    address_id = models.IntegerField(primary_key=True)
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    landmark = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone_no = models.ForeignKey(RegUser, to_field='phone_no', on_delete=models.CASCADE)
                                                                                               
class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    order_date = models.DateField((u"Order date"), auto_now_add=True)
    order_time = models.TimeField((u"Order time"), auto_now_add=True)
    address = models.CharField(max_length=500)
    phone_no = models.ForeignKey(RegUser, to_field='phone_no', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_id)
