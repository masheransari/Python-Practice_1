class ParentClassA:
    __quantity: int = 0

    def __init__(self, quantity):
        self.__quantity = quantity


    def getResult(self):
        return self.__quantity * self.__quantity
