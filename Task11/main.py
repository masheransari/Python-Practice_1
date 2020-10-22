from ChildClass import ChildClass
from ParentClassA import ParentClassA
from ParentClassB import ParentClassB
from ParentClassC import ParentClassC

quantity = 5

childA = ParentClassA(quantity)
childB = ParentClassB(quantity)
childC = ParentClassC(quantity)

print(childA.getResult())
print(childB.getResult())
print(childC.getResult())
