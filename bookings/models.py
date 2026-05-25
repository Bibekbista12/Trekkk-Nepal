from django.db import models
from django.conf import settings
from treks.models import Trek

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    trek        = models.ForeignKey(Trek, on_delete=models.CASCADE, related_name='bookings')
    trek_date   = models.DateField()
    num_people  = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_id  = models.CharField(max_length=200, blank=True)
    special_req = models.TextField(blank=True, help_text="Any special requirements?")
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.trek.price * self.num_people
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} — {self.trek.name} ({self.trek_date})"