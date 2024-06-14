from Location import Location
from Employee import Employee
from Shift import Shift
from ortools.sat.python import cp_model

class ScheduleManager:
    #weekly schedule
    def __init__(self,Days):
        self.Days = Days


def create_schedule(num_days, shifts, employees):
    model = cp_model.CpModel()

    num_workers = len(employees)
    roles = ['cashier', 'cook']

    # Create shift variables
    shift_vars = {}
    for worker in range(num_workers):
        for day in range(num_days):
            for shift in shifts[day]:
                shift_id = shift.shift_id
                for role in roles:
                    shift_vars[(worker, day, shift_id, role)] = model.NewBoolVar(f'shift_w{worker}_d{day}_s{shift_id}_{role}')

    # Constraints: Each shift on each day must be covered by the required roles
    for day in range(num_days):
        for shift in shifts[day]:
            shift_id = shift.shift_id
            for role, slots in shift.roles_required.items():
                model.Add(sum(shift_vars[(worker, day, shift_id, role)] for worker in range(num_workers)) == slots)

    # Constraints: Respect workers' availability, roles, and working hours
    for worker in range(num_workers):
        for day in range(num_days):
            for shift in shifts[day]:
                shift_id = shift.shift_id
                if not employees[worker].availability.get(day, {}).get(shift_id, 0):
                    for role in roles:
                        model.Add(shift_vars[(worker, day, shift_id, role)] == 0)
                for role in roles:
                    if role not in employees[worker].roles:
                        model.Add(shift_vars[(worker, day, shift_id, role)] == 0)

    # Constraints: Each worker must meet their minimum and maximum hours requirements
    for worker in range(num_workers):
        total_hours = sum(shift_vars[(worker, day, shift.shift_id, role)] * shift.duration 
                          for day in range(num_days) 
                          for shift in shifts[day] 
                          for role in roles)
        model.Add(total_hours >= employees[worker].min_hours)
        model.Add(total_hours <= employees[worker].max_hours)

    # Objective: Distribute shifts as evenly as possible among workers
    total_shifts = sum(shift_vars[(worker, day, shift.shift_id, role)] 
                       for worker in range(num_workers) 
                       for day in range(num_days) 
                       for shift in shifts[day] 
                       for role in roles)
    min_shifts = total_shifts // num_workers
    max_shifts = min_shifts + 1
    for worker in range(num_workers):
        num_shifts = sum(shift_vars[(worker, day, shift.shift_id, role)] 
                         for day in range(num_days) 
                         for shift in shifts[day] 
                         for role in roles)
        model.Add(min_shifts <= num_shifts)
        model.Add(num_shifts <= max_shifts)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Output the schedule
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        schedule = Schedule(num_days)
        for worker in range(num_workers):
            for day in range(num_days):
                for shift in shifts[day]:
                    shift_id = shift.shift_id
                    for role in roles:
                        if solver.Value(shift_vars[(worker, day, shift_id, role)]):
                            if role not in schedule.schedule[day]:
                                schedule.schedule[day][role] = []
                            schedule.schedule[day][role].append({
                                'employee': employees[worker].name,
                                'shift_id': shift_id,
                                'start_time': shift.start_time,
                                'end_time': shift.end_time
                            })
        return schedule
    else:
        print('No solution found.')
        return None   

    def create_shift(day, start_time, end_time):
        try:
            day.add_shift(start_time, end_time)
            print(f"Shift added: {day.shifts[-1]}")
        except ValueError as e:
            print(f"Error: {e}")

    def display_shifts(day):
        print(f"Shifts for {day.date.strftime('%Y-%m-%d')}:")
        for shift in day.get_shifts():
            print(shift)

