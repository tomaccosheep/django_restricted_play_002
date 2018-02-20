from django.db import models

# Create your models here.

class Play_Project(models.Model):
    id = models.AutoField(primary_key=True)
    unique_id = models.CharField(null=True, max_length=32, unique=True)
    con_001 = models.CharField(max_length=16, null=True)
    def __str__(self):
        return self.unique_id
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
