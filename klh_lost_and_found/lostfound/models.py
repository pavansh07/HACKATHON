from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now  # Import timezone-aware now

class LostFoundItem(models.Model):
    STATUS_CHOICES = (
        ('lost', 'Lost'),
        ('found', 'Found'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
