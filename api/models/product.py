from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Product(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

    def __str__(self):
      # This must return a string
      return f"The product named '{self.name}' is {self.price} dollars. It is {self.brand} that it is brand."

    def as_dict(self):
      """Returns dictionary version of Product models"""
      return {
          'id': self.id,
          'name': self.name,
          'image': self.image,
          'brand': self.brand,
          'category': self.category,
          'description': self.description,
          'rating': self.rating,
          'numReviews': self.numReviews,
          'price': self.price,
          'countInStock': self.countInStock,
          '_id': self._id
      }

