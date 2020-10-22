class Employee:
    def __init__(self, id, name, age, salMonthly):
        self.id = id
        self.name = name
        self.age = age
        self.salMonthly = salMonthly
        self.annual_sal = 0

    def AnnualSalary(self):
        self.annual_sal = self.salMonthly * 12

    def SetAge(self):
        if self.age < 25:
            print("Your age is below 25.")
            new_age = int(input("Enter your new age in between 25 and 50 years: "))
            self.age = new_age
        elif self.age > 50:
            print("You are way past your retirement sir.")
            new_age = int(input("Enter your new age in between 25 and 50 years: "))
            self.age = new_age

    def SetSalary(self):
        sal_condition = input("Do you want to set new value of employee salary?: ")
        if sal_condition == "yes" or sal_condition == "Yes":
            new_sal = int(input("Enter the new value for employee salary: "))
            self.salMonthly = new_sal
        else:
            pass

    def print(self):
        return "The Employee Id of Employee is %s. \nThe name of Employee is %s.\nThe Age of Employee is %s." \
               "\nThe Monthly Salary is %s.\nThe Annual Salary is %s." \
               % (str(self.id), str(self.name), str(self.age), str(self.salMonthly), str(self.annual_sal))
