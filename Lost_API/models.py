from django.db import models

class ApiData(models.Model):
    FOUND_CHOICES = [
        ('True', 'True'),
        ('False', 'False'),
    ]

    found = models.CharField(
        max_length=5,
        choices=FOUND_CHOICES,
        default='False',  # Optional: set a default value
        blank=True,  # Optional: allow blank if required
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    phone = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads/')  # Save images in 'media/uploads/' directory
    data = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    comments = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
