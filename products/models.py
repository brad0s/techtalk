from django.db import models

# Create your models here.
class Product(models.Model):
  name        = models.CharField(max_length=25)
  description = models.TextField()
  price       = models.DecimalField(max_digits=10, decimal_places=2)
  image       = models.ImageField(upload_to='product_images', default='product-default.png')

  def __str__(self):
    return f"{self.id} - {self.name}"