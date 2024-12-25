from django.db import models
from app.models import Clients


class Products(models.Model):
    tenant = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name="products")  # Linking Products to a Tenant
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
   

    def __str__(self):
        return self.name
