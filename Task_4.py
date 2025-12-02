hourly_payment = 400

class EmployeeSalary:
    def __init__(self, name, rest_days, hours = None, email = None):
        self.name = name
        self.rest_days = rest_days
        self.hours = hours if hours is not None else self.get_hours(rest_days)
        self.email = email if email is not None else self.get_email(name)
        

    @classmethod
    def get_hours(cls, rest_days):
        return (7 - rest_days) * 8
    
    @classmethod
    def get_email(cls, name):
        return f"{name}@email.com"
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
    
    def salary(self, hours, hourly_payment):
        return self.hours * self.hourly_payment
        
    
