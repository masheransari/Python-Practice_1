import DesktopModel as Desktop

from Computer import Computer
from Laptop import Laptop
from MiniComputer import MiniComputer
from SuperComputer import SuperComputer

computer = MiniComputer()
print(computer.billing())


laptop = Laptop()
print(laptop.billing())

superComputer = SuperComputer()
print(superComputer.billing())

desktop = Desktop.DesktopModel()
desktop.set_company("company Name")
print(desktop.billing())
