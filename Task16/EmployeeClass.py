from CeoClass import CeoClass
from ManagerClass import ManagerClass


class EmployeeClass(CeoClass, ManagerClass):
    def showCompanyEmployees(self):
        print("CEO Name     :", self.ceoName)
        print("Manager Name :", self.managerName)
