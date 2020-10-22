from Computer import Computer
from MainFrame import MainFrame
from MiniComputer import MiniComputer

print("Method Overriding")
print("Simple calling parent function which is in Computer Class")
miniComptuer = MiniComputer(25000,"Smart Mini Computer")
print(miniComptuer.billing())
print("\n--------------------------------------------\n")
print("Method overriding while defining in MainFrame class..")
mainFrame = MainFrame(110000,"Smart Main Frame Computer")
print(mainFrame.billing())

