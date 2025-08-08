from django.db import models
from django.utils.text import slugify

# Create your models here.


class InteriorWork(models.Model):
    INTERIOR_TYPES = [
        ('Living Room', 'Living Room'),
        ('Bedroom', 'Bedroom'),
        ('Kitchen', 'Kitchen'),
        ('Office', 'Office'),
        ('Bathroom', 'Bathroom'),
        ('Dining Area', 'Dining Area'),
        ('Commercial Space', 'Commercial Space'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    interior_type = models.CharField(max_length=50, choices=INTERIOR_TYPES)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    completion_date = models.DateField()

    image1 = models.ImageField(upload_to='interior_works/', verbose_name='Main Image')  
    image2 = models.ImageField(upload_to='interior_works/', blank=True, null=True)
    image3 = models.ImageField(upload_to='interior_works/', blank=True, null=True)
    image4 = models.ImageField(upload_to='interior_works/', blank=True, null=True)
    image5 = models.ImageField(upload_to='interior_works/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title