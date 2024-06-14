from django.db import models
from django.contrib.postgres.fields import JSONField
from .location import Location
from .employee import Employee

class Shift(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_slots = models.IntegerField()
    roles_required = JSONField()  # Store roles_required as a JSON dict
    assigned = models.ManyToManyField(Employee, related_name='shifts')
    
    def __str__(self):
        return f"Shift: {self.start_time} - {self.end_time}"

    def check_roles_fulfilled(self):
        """
        Check if the required roles are fulfilled by the assigned employees.

        Returns:
            bool: True if all roles required are fulfilled, False otherwise.
        """
        # Initialize a dictionary to count the number of employees per role
        roles_count = {role: 0 for role in self.roles_required}

        # Count the number of employees assigned to each role
        for employee in self.assigned.all():
            for role in employee.roles:
                if role in roles_count:
                    roles_count[role] += 1

        # Check if the count of each role meets or exceeds the required amount
        for role, required_amount in self.roles_required.items():
            if roles_count.get(role, 0) < required_amount:
                return False

        return True
