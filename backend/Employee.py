from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    scheduled_hours = models.FloatField(default=0)
    min_hours = models.FloatField()
    max_hours = models.FloatField()
    roles = ArrayField(models.CharField(max_length=50))
    availability = JSONField()  # Store availability as a JSON dict
    assigned_shifts = JSONField(default=list)  # Store assigned shifts as a JSON list

    def can_work(self, day, shift_id, role):
        if str(day) not in self.availability or str(shift_id) not in self.availability[str(day)]:
            return False
        if role not in self.roles:
            return False
        return True

    def has_min_hours(self):
        """
        Checks if the minimum amount of hours has been met.
        Returns:
            bool: True if the minimum hours have been met, False otherwise.
        """
        return self.scheduled_hours >= self.min_hours

    def __str__(self):
        return self.name