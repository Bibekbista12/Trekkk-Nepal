from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Trek(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy',     'Easy'),
        ('moderate', 'Moderate'),
        ('hard',     'Hard'),
    ]
    REGION_CHOICES = [
        ('everest',   'Everest Region'),
        ('annapurna', 'Annapurna Region'),
        ('langtang',  'Langtang Region'),
        ('manaslu',   'Manaslu Region'),
        ('other',     'Other'),
    ]

    agency      = models.ForeignKey(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE,
                    limit_choices_to={'role': 'agency'},
                    related_name='treks'
                  )
    name        = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    difficulty  = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    duration    = models.PositiveIntegerField(help_text="Number of days")
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    max_group   = models.PositiveIntegerField(default=12)
    region      = models.CharField(max_length=20, choices=REGION_CHOICES)
    cover_image = models.ImageField(upload_to='treks/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('trek-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-is_featured', '-created_at']


class TrekImage(models.Model):
    trek        = models.ForeignKey(Trek, on_delete=models.CASCADE, related_name='images')
    image       = models.ImageField(upload_to='treks/gallery/')
    caption     = models.CharField(max_length=200, blank=True)
    is_cover    = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.trek.name}"