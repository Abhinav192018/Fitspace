from django.db import models
from django.utils.text import slugify

# Create your models here.

class banner_Image(models.Model):
    image=models.ImageField(upload_to="Banner_image/")
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)


class GalleryImage(models.Model):
    image=models.ImageField(upload_to='gallery')



class InteriorWork(models.Model):
    INTERIOR_TYPES = [
        ('Sliding Wardrobe', 'Sliding Wardrobe'),
        ('Media Wall', 'Media Wall'),
        ('Fitted Wardrobe', 'Fitted Wardrobe'),
        ('Fitted Kitchens', 'Fitted Kitchens'),
        ('Loft Wardrobes', 'Loft Wardrobes'),
        ('Home Office', 'Home Office'),



        ('Living Room', 'Living Room'),
        ('Bedroom', 'Bedroom'),
        ('Kitchen', 'Kitchen'),
        ('Office', 'Office'),
        ('Bathroom', 'Bathroom'),
        ('Dining Area', 'Dining Area'),
        ('Commercial Space', 'Commercial Space'),
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
    


from django.db import models

class Blog(models.Model):
    CATEGORIES = [


        ('Sliding Wardrobe', 'Sliding Wardrobe'),
        ('Media Wall', 'Media Wall'),
        ('Fitted Wardrobe', 'Fitted Wardrobe'),
        ('Fitted Kitchens', 'Fitted Kitchens'),
        ('Loft Wardrobes', 'Loft Wardrobes'),
        ('Home Office', 'Home Office'),


        ('Living Room', 'Living Room'),
        ('Bedroom', 'Bedroom'),
        ('Kitchen', 'Kitchen'),
        ('Office', 'Office'),
        ('Bathroom', 'Bathroom'),
        ('Dining Area', 'Dining Area'),
        ('Commercial Space', 'Commercial Space'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    short_description = models.CharField(max_length=255) 
    author_name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to="authors/", blank=True, null=True)  
    published_date = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to="blog_images/")  

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Featured_Blog(models.Model):
    CATEGORIES = [
        ('Sliding Wardrobe', 'Sliding Wardrobe'),
        ('Media Wall', 'Media Wall'),
        ('Fitted Wardrobe', 'Fitted Wardrobe'),
        ('Fitted Kitchens', 'Fitted Kitchens'),
        ('Loft Wardrobes', 'Loft Wardrobes'),
        ('Home Office', 'Home Office'),


        
        ('Living Room', 'Living Room'),
        ('Bedroom', 'Bedroom'),
        ('Kitchen', 'Kitchen'),
        ('Office', 'Office'),
        ('Bathroom', 'Bathroom'),
        ('Dining Area', 'Dining Area'),
        ('Commercial Space', 'Commercial Space'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    short_description = models.CharField(max_length=255) 
    author_name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to="authors/", blank=True, null=True)  
    published_date = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to="blog_images/")  

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    

class Services(models.Model):
    image=models.ImageField(upload_to="services/")
    title=models.CharField(max_length=200)
    description=models.TextField()