from FatherClass import FatherClass
from MotherClass import MotherClass


class SonClass(FatherClass, MotherClass):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
