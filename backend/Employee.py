class Employee:

    def __init__(self,name, scheduledHours, minHours, maxHours):
        self.scheduled = scheduledHours
        self.minHours = minHours
        self.maxHours = maxHours

    def get_minHours(self):
        return self.minHours
    def set_minHours(self, hours):
        self.minHours = hours

    def get_maxHours(self):
        return self.maxHours
    def set_maxHours(self,hours):
        self.maxHours = hours

    def get_Name(self):
        return self.name
    def set_Name(self,name):
        self.name = name

    def get_scheduledHours(self):
        return self.scheduleHours

    def set_scheduledHours(self,hours):
        self.scheduleHours = hours

#check if the user has met min hours for the week
    def hasMinHours(self):
        if (self.scheduleHours >= self.minHours):
            return True
        else:
            return False

