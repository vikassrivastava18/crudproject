import uuid

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


Category = (
        ('el', 'Electronics'),
        ('gr', 'Grocery'),
        ('fu', 'Furniture'),
        ('bo', 'Books'),
    )


class Product(models.Model):
    # Fields
    name = models.CharField(max_length=50, help_text='Enter name of the product')
    category = models.CharField(
        max_length=2,
        choices=Category,
        blank=True,
        help_text='Product Category'
    )

    # Metadata
    class Meta:
        ordering = ['-name']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name


class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for particular product instance')
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    purchased_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id


