from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Case(models.Model):
    CATEGORY_CHOICES = [
        ('Civil', 'Civil'),
        ('Criminal', 'Criminal'),
        ('Family', 'Family'),
        ('Divorce', 'Divorce'),
        ('Corporate', 'Corporate'),
        ('Intellectual Property', 'Intellectual Property'),
        ('Employment', 'Employment'),
        ('Tax', 'Tax'),
        ('Real Estate', 'Real Estate'),
        ('Bankruptcy', 'Bankruptcy'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"

class Massage(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender.username}: {self.text[:30]}"
    

    