from ParentClassA import ParentClassA
from ParentClassB import ParentClassB
from ParentClassC import ParentClassC


class ChildClass(ParentClassA, ParentClassB, ParentClassC):
    quantity: int

    def __init__(self, quantity):
        super().__init__(quantity)
