from ClassA import ClassA


class ClassC(ClassA):
    __instance = None

    def __init__(self):
        pass

    def printData(self):
        print("Print in Class C Inherit with Class A")

    @staticmethod
    def getClassC():
        if ClassC.__instance is None:
            ClassC.__instance = ClassC()
        return ClassC.__instance
