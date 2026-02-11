from django.db import models


class Workshop(models.Model):
    TYPE_CHOICES = [
        ('stem', 'STEM Workshop'),
        ('robotics', 'Robotics Workshop'),
        ('iot', 'IoT Workshop'),
        ('science', 'Science Workshop'),
        ('coding', 'Coding Workshop'),
        ('electronics', 'Electronics Workshop'),
    ]
    TARGET_CHOICES = [
        ('play_school', 'Play School'),
        ('school', 'School'),
        ('college', 'College'),
    ]

    title = models.CharField(max_length=300)
    workshop_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    target_audience = models.CharField(max_length=20, choices=TARGET_CHOICES, default='school')
    description = models.TextField()
    duration = models.CharField(max_length=100, help_text='e.g. "2 Hours", "Full Day"')
    max_students = models.IntegerField(default=30)
    price_per_student = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='workshops/', blank=True, null=True)
    features = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class WorkshopBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    workshop = models.ForeignKey(Workshop, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    school_name = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    preferred_date = models.DateField(blank=True, null=True)
    number_of_students = models.IntegerField()
    workshop_type = models.CharField(max_length=50, choices=Workshop.TYPE_CHOICES, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.school_name} - {self.get_status_display()}'
