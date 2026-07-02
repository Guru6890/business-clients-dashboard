from django.db import models

import uuid

# Create your models here.

class Invoice(models.Model):
    class STATUS(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        SENT = 'sent', 'Sent'
        PAID = 'paid', 'Paid'
        OVERDUE = 'overdue', 'Overdue'
        VOID = 'void', 'Void'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    invoice_number = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey('clients.Company', on_delete=models.RESTRICT, related_name='invoices')
    status = models.CharField(max_length=7, choices=STATUS.choices, default=STATUS.DRAFT)
    issue_date = models.DateField()
    due_date = models.DateField()
    strip_invoice_id = models.CharField(max_length=100, unique=True, null=True)
    