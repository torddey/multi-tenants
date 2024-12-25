from django.db import models
from app.models import Clients


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
   

    def __str__(self):
        return self.name
