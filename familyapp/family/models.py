from django.db import models

# Create your models here.

class Family(models.Model):
    family_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    created_at = models.TimeField()

    
