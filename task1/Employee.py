class Employee:
    def __init__(self):
        self.empName = ""
        self.empNum = 0
        self.empSalary = 0.0

    def updateUserData(self, name, empNum, salary):
        self.empName = name
        self.empNum = empNum
        self.empSalary = salary

    def printDetails(self):
        print("Name:\t\t" + str(self.empName))
        print("Emp Id:\t\t" + str(self.empNum))
        print("Emp Salary:\t\t" + str(self.empSalary))
