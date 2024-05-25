class Day:

    def __init__(self,date,openTime,closeTime,workersPershift,hoursPerShift,shiftsPerDay,isClosed):
        self.date = date
        self.openTime = openTime
        self.closeTime = closeTime
        self.workersPershift = workersPershift
        self.hoursPerShift = hoursPerShift
        self.shiftsPerDay = shiftsPerDay
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

    def get_hoursPerShift(self):
        return self.hoursPerShift
    def set_hoursPerShift(self,hours):
        self.hoursPerShift = hours
    def get_shiftsPerDay(self):
        return self.shiftsPerDay
    def set_shiftsPerDay(self,amount_of_shifts):
        self.shiftsPerDay = amount_of_shifts
    def get_isClosed(self):
        return self.isClosed
    def set_isClosed(self,isClosed):
        self.isClosed = isClosed