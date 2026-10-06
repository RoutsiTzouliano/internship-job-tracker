from django.db import models

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
