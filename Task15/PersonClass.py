from EmployeeClass import EmployeeClass
from ManagerClass import ManagerClass


class PersonClass(ManagerClass, EmployeeClass):
    def __init__(self, emp_id, name, age, sal_mon, post, points):
        self.points = points
        ManagerClass.__init__(self, emp_id, name, age, sal_mon)
        EmployeeClass.__init__(self, post, emp_id, name, age, sal_mon)
        print(self.sal_mon)
