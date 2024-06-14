from datetime import datetime, time, timedelta
from collections import defaultdict


class Employee:

    def __init__(self, name, availability, scheduledHours, minHours, maxHours, roles):
        self.name = name
        self.scheduledHours = scheduledHours
        self.minHours = minHours
        self.maxHours = maxHours
        self.roles = roles
        self.availability = availability
        self.assignedShifts = []
    def can_work(self,day, shift_id,role):
        if day not in self.avaiability or shift_id not in self.availability[day]:
            return False 
        if role not in self.roles:
            return False
        return True
    
    def get_minHours(self):
        return self.minHours

    def set_minHours(self, hours):
        self.minHours = hours

    def get_maxHours(self):
        return self.maxHours

    def set_maxHours(self, hours):
        self.maxHours = hours

    def get_Name(self):
        return self.name

    def set_Name(self, name):
        self.name = name

    def get_scheduledHours(self):
        return self.scheduledHours

    def set_scheduledHours(self, hours):
        self.scheduledHours = hours

    def get_roles(self):
        return self.roles

    def set_roles(self, roles):
        self.roles = roles

    # Check if the employee has met the minimum hours for the week
    def hasMinHours(self):
        """""
            checks if their minimum amount of hours has been met
            Returns:
                bool - true or false
        """

        return self.scheduledHours >= self.minHours
