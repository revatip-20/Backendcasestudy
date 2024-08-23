from django.contrib.auth.models import User
from django.db import models

class ServiceRequest(models.Model):
    CUSTOMER_SERVICE = 'CS'
    TECHNICAL_SUPPORT = 'TS'
    BILLING = 'B'

    REQUEST_TYPE_CHOICES = [
        (CUSTOMER_SERVICE, 'Customer Service'),
        (TECHNICAL_SUPPORT, 'Technical Support'),
        (BILLING, 'Billing'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=2, choices=REQUEST_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_request_type_display()}"
