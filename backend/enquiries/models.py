from django.db import models


class Enquiry(models.Model):
    TYPE_CHOICES = [
        ('general', 'General Enquiry'),
        ('product', 'Product Enquiry'),
        ('bulk', 'Bulk Order Enquiry'),
        ('oem', 'OEM Enquiry'),
        ('odm', 'ODM Enquiry'),
        ('distributor', 'Distributor Enquiry'),
        ('retailer', 'Retailer Enquiry'),
        ('school', 'School Enquiry'),
        ('workshop', 'Workshop Enquiry'),
        ('tuition', 'Tuition Enquiry'),
    ]
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('responded', 'Responded'),
        ('closed', 'Closed'),
    ]

    enquiry_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Enquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.get_enquiry_type_display()}'


class SchoolInquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
        ('closed', 'Closed'),
    ]

    school_name = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    number_of_students = models.IntegerField(blank=True, null=True)
    interested_in = models.JSONField(default=list, blank=True, help_text='List of interests: kits, workshops, tuition')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'School Inquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.school_name} - {self.contact_person}'
