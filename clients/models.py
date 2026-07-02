from django.db import models

import uuid

# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    strip_customer_id = models.CharField(max_length=100, unique=True, null=True)
    billing_address = models.TextField()

class CompanyMembership(models.Model):
    class Roles(models.TextChoices):
        OWNER = 'owner', 'Owner'
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'
        MEMBER = 'member', 'Member'
        VIEWER = 'viewer', 'Viewer'

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    company = models.ForeignKey('clients.Company', on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=Roles.choices, default=Roles.MEMBER)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'company'],
                name='unique_user_company'
            )
        ]