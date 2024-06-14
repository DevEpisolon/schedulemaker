from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    weekly_hours = models.IntegerField()

    def __str__(self):
        return self.name
