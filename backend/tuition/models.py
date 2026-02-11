from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Verification'),
        ('verified', 'Verified'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    qualification = models.CharField(max_length=300)
    experience_years = models.IntegerField(default=0)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-rating', '-created_at']

    def __str__(self):
        return self.full_name


class TuitionApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('matched', 'Teacher Matched'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    CLASS_CHOICES = [
        ('nursery', 'Nursery'),
        ('lkg', 'LKG'),
        ('ukg', 'UKG'),
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
        ('11', 'Class 11'),
        ('12', 'Class 12'),
    ]

    parent_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    student_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    subjects = models.ManyToManyField(Subject, related_name='applications')
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    preferred_time = models.CharField(max_length=200, blank=True, help_text='e.g. "Morning 9-11 AM"')
    message = models.TextField(blank=True)
    assigned_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.parent_name} - {self.student_name} ({self.get_status_display()})'


class TeacherRegistration(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    qualification = models.CharField(max_length=300)
    experience_years = models.IntegerField(default=0)
    subjects = models.CharField(max_length=500, help_text='Comma-separated subjects')
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=100)
    resume = models.FileField(upload_to='teacher_resumes/', blank=True, null=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} - {self.get_status_display()}'
