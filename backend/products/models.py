from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    icon_name = models.CharField(max_length=50, blank=True, help_text='React icon name')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    AGE_GROUP_CHOICES = [
        ('3-5', '3-5 Years'),
        ('5-8', '5-8 Years'),
        ('8-12', '8-12 Years'),
        ('12-16', '12-16 Years'),
        ('16+', '16+ Years'),
    ]
    TARGET_CHOICES = [
        ('play_school', 'Play School'),
        ('school', 'School'),
        ('college', 'College'),
        ('home', 'Home / Parents'),
        ('all', 'All'),
    ]
    STOCK_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('coming_soon', 'Coming Soon'),
    ]

    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    features = models.JSONField(default=list, blank=True, help_text='List of feature strings')
    learning_outcomes = models.JSONField(default=list, blank=True)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)
    target_audience = models.CharField(max_length=20, choices=TARGET_CHOICES, default='all')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_bulk_quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='products/')
    gallery_images = models.JSONField(default=list, blank=True, help_text='List of image URLs')
    is_featured = models.BooleanField(default=False)
    is_eco_friendly = models.BooleanField(default=True)
    stock_status = models.CharField(max_length=20, choices=STOCK_CHOICES, default='in_stock')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
