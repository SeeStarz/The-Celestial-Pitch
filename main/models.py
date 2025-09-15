import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('gear', 'Gear'),
        ('relic', 'Relic'),
        ('consumable', 'Consumable'),
        ('powerup', 'Power Up'),
        ('special', 'Special'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    base_price = models.IntegerField()
    description = models.TextField()
    icon = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=31)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
