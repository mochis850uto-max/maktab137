class Employee:
    def __init__(self, name: str, base_salary: int):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
    
    def info(self):
        print(f"Employee: {self.name}, Base salary: {self.base_salary}")

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus: int):
        super().__init__(name, base_salary)
        self.bonus = bonus
    
    def calculate_bonus(self):
        general_salary = self.base_salary + self.bonus
        return general_salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hourly_rate, hours_worked):
        super().__init__(name, base_salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_hour(self):
        result = self.hourly_rate * self.hours_worked
        return result

employee = Employee("John", 6000)
full_time = FullTimeEmployee("Peter", 6000, 586)
part_time = PartTimeEmployee("Walter", 3000, 12.5, 8)
print(employee.calculate_salary())
employee.info()
print(f"{full_time.name} Total salary with bonus : {full_time.calculate_bonus()}")
print(f"{part_time.name} daily salary : {part_time.calculate_hour()}")