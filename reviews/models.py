from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from treks.models import Trek

class Review(models.Model):
    trek       = models.ForeignKey(Trek, on_delete=models.CASCADE, related_name='reviews')
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating     = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('trek', 'user')

    def __str__(self):
        return f"{self.user.username} — {self.trek.name} {self.rating}/5"