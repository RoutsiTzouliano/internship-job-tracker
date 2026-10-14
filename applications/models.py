from django.db import models
from django.conf import settings

# Create your models here.
class Application(models.Model):

    STATUS_CHOICES=[
        ("applied","Applied"),
        ("interview","Interview"),
        ("accepted","Accepted"),
        ("rejected","Rejected")
    ]

    company=models.CharField(max_length=50)
    position=models.CharField(max_length=50)

    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="applied"
    )

    application_date=models.DateField()

    notes=models.TextField(
        blank=True
        )

    created_at=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.company},{self.position}"

#company model 
class Company(models.Model):
    name = models.CharField(max_length=100)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

#job posting model
class JobPosting(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title