from django.db import models
from django.utils import timezone
from Business import Business
from Shift import Shift
from BusinessHours import BusinessHours

class Day(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    date = models.DateField()
    workers_per_shift = models.IntegerField()
    min_hours_per_shift = models.IntegerField()
    max_hours_per_shift = models.IntegerField()
    min_shifts_per_day = models.IntegerField()
    max_shifts_per_day = models.IntegerField()
    is_closed = models.BooleanField(default=False)

    def add_shift(self, start_time, end_time):
        if self.is_closed:
            raise ValueError("Cannot add shifts to a closed day.")

        open_time, close_time = self.get_business_hours()
        
        if not (open_time <= start_time < end_time <= close_time):
            raise ValueError("Shift time must be within store hours.")
        
        shift_duration = end_time - start_time
        if not (self.min_hours_per_shift <= shift_duration <= timezone.timedelta(hours=self.max_hours_per_shift)):
            raise ValueError("Shift duration must be within allowed hours per shift.")
        
        if self.shifts.count() >= self.max_shifts_per_day:
            raise ValueError("Cannot add more shifts, maximum shifts per day reached.")

        shift = Shift(day=self, start_time=start_time, end_time=end_time)
        shift.save()

    def get_shifts(self):
        return self.shifts.all()

    def get_business_hours(self):
        weekday = self.date.weekday()
        business_hours = BusinessHours.objects.filter(business=self.business, weekday=weekday).first()
        if business_hours:
            return business_hours.open_time, business_hours.close_time
        else:
            return None, None

    def __str__(self):
        return f"Date: {self.date.strftime('%Y-%m-%d')}, Shifts: {self.shifts.count()}"
