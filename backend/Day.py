from datetime import datetime, time, timedelta

class Day:

    def __init__(self,date,openTime,closeTime,workersPershift,minHoursPerShift, maxHoursPerShift,minShiftsPerDay,maxShiftsPerDay,isClosed):
        self.date = date
        self.openTime = openTime
        self.closeTime = closeTime
        self.workersPershift = workersPershift
        self.minHoursPerShift = minHoursPerShift
        self.maxHoursPerShift = maxHoursPerShift
        self.minShiftsPerDay = minShiftsPerDay
        self.isClosed = isClosed
   
    def add_shift(self, start_time, end_time):
        if self.is_closed:
            raise ValueError("Cannot add shifts to a closed day.")
        
        if not (self.open_time <= start_time < end_time <= self.close_time):
            raise ValueError("Shift time must be within store hours.")
        
        shift_duration = datetime.combine(self.date, end_time) - datetime.combine(self.date, start_time)
        if not (self.min_hours_per_shift <= shift_duration <= timedelta(hours=self.max_hours_per_shift)):
            raise ValueError("Shift duration must be within allowed hours per shift.")
        
        if len(self.shifts) >= self.max_shifts_per_day:
            raise ValueError("Cannot add more shifts, maximum shifts per day reached.")

        shift = Shift(self, start_time, end_time)
        self.shifts.append(shift)

    def get_shifts(self):
        return self.shifts
 
    def get_date(self):
        return self.date
    def set_date(self,date):
        self.date = date
   
    def get_openTime(self):
        return self.openTime
    def set_openTime(self,time):
        self.time = time

    def get_closeTime(self):
        return self.closeTime
    def set_closeTime(self,time):
        self.closeTime = time

    def get_workersPerShift(self):
        return self.workersPerShift
    def set_workersPerShift(self,amount_of_workers):
        self.workersPerShift = amount_of_workers

    def get_minHoursPerShift(self):
        return self.minHoursPerShift
    def set_minHoursPerShift(self,hours):
        self.minHoursPerShift = hours

    def get_maxHoursPerShift(self):
        return self.maxHoursPerShift
    def set_maxHoursPerShift(self,hours):
        self.maxHoursPerShift = hours

    def get_minShiftsPerDay(self):
        return self.minShiftsPerDay
    def set_minShiftsPerDay(self,amount_of_shifts):
        self.minShiftsPerDay = amount_of_shifts
    
    def get_maxShiftsPerDay(self):
        return self.get_maxShiftsPerDay
    def set_maxShiftsPerDay(self,amount_of_shifts):
        self.get_maxShiftsPerDay = amount_of_shifts


    def get_isClosed(self):
        return self.isClosed
    #boolean True or False
    def set_isClosed(self,isClosed):
        self.isClosed = isClosed

    def __str__(self):
        open_time_str = self.open_time.strftime('%H:%M') if self.open_time else 'Not Set'
        close_time_str = self.close_time.strftime('%H:%M') if self.close_time else 'Not Set'
        return f"Date: {self.date.strftime('%Y-%m-%d')}, Open Time: {open_time_str}, Close Time: {close_time_str}, Shifts: {len(self.shifts)}"