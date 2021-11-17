from django.db import models

class Product(models.Model):
    name       = models.CharField(max_length=100)
    code       = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'