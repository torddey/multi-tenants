from django.db import models
from django_tenants.models import DomainMixin, TenantMixin

# Create Tenants with domain 

class Clients(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)


class Domain(DomainMixin):
    pass
    