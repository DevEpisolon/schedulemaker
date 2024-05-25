from Employee import Employee
class Shift:
    def __init__(self,startTime,endTime,availableSlots,rolesRequired):
        self.startTime = startTime
        self.endTime = endTime
        self.availableSlots = availableSlots
        self.rolesRequired = rolesRequired

    def get_startTime(self):
        return self.startTime
    def set_startTime(self,time):
        self.time = time

    def get_endTime(self):
        return self.endTime
    def set_endTime(self,time):
        self.endTime = time

    def get_availableSlots(self):
        return self.availableSlots
    def set_availableSlots(self,slots):
        self.availableSlots = slots

    def get_rolesRequired(self):
        return self.rolesRequired
    def set_rolesRequired(self, roles):
        self.rolesRequired = roles
    #Check if has all roles needed and fufilled
    def check_roles_fulfilled(roles_required, employees_assigned):
        """
        Check if the required roles are fulfilled by the assigned employees.

        Args:
        roles_required (dict): A dictionary with roles as keys and the number of each role required as values.
                               Example: {'cook': 2, 'cashier': 1}
        employees_assigned (list): A list of Employee objects.

        Returns:
        bool: True if all roles required are fulfilled, False otherwise.
        """
        # Initialize a dictionary to count the number of employees per role
        roles_count = {role: 0 for role in roles_required}

        # Count the number of employees assigned to each role
        for employee in employees_assigned:
            for role in employee.get_roles():
                if role in roles_count:
                    roles_count[role] += 1

        # Check if the count of each role meets or exceeds the required amount
        for role, required_amount in roles_required.items():
            if roles_count.get(role, 0) < required_amount:
                return False

        return True