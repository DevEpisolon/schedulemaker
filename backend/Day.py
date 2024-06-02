from datetime import datetime, time, timedelta

class Day:

    def __init__(self,date,openTime,closeTime,workersPershift,minHoursPerShift, maxHoursPerShift,minShiftsPerDay,maxShiftsPerDay,isClosed):
        self.date = date
        self.openTime = openTime
        self.closeTime = closeTime
        self.workersPershift = workersPershift
        self.minHoursPerShift = minHoursPerShift
        self.maxHoursPerShift = maxHoursPershift
        self.minShiftsPerDay = minShiftsPerDay
        self.isClosed = isClosed
   
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
        openTime_str = self.openTime.strftime('%Y-%m-%d %H:%M') if self.openTime else 'Not Set'
        closeTime_str = self.closetime.strftime('%Y-%m-%d %H:%M') if self.closeTime else 'Not Set'
        return f"Date: {self.date.strftime('%Y-%m-%d')}, Start Time: {openTime_str}, End Time: {closeTime_str}"
