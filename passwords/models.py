from django.db import models

# Create your models here.
class Passwords(models.Model):
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.website} - {self.username}"