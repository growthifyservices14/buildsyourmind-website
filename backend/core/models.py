from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default='Builds Your Mind')
    tagline = models.CharField(max_length=500, blank=True)
    email = models.EmailField(default='info@buildsyourmind.in')
    phone = models.CharField(max_length=20, default='+91 91097 11321')
    whatsapp = models.CharField(max_length=20, default='+91 91097 11321')
    address = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name


class Testimonial(models.Model):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
        ('school', 'School'),
        ('distributor', 'Distributor'),
        ('student', 'Student'),
    ]
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    role_label = models.CharField(max_length=200, blank=True, help_text='Custom role label e.g. "Principal, ABC School"')
    content = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.role}'


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('product', 'Product'),
        ('event', 'Event'),
        ('team', 'Team'),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
