from django.db import models

# Create your models here.
class Generator(models.Model):
    password = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.password