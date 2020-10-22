class ParentClassC:
    __quantity: int

    def __init__(self, quantity):
        self.__quantity = quantity

    def getResult(self):
        return self.__quantity * self.__quantity * self.__quantity * self.__quantity
