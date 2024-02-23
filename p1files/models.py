from django.db import models


# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='template/carousel_images/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='template/product_images/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
