from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Furniture(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pict/")
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

