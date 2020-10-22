from ClassB import ClassB


class ClassD(ClassB):
    __instance = None

    def __init__(self):
        pass

    def printData(self):
        print("Print in Class D Inherit with Class B")

    @staticmethod
    def getClassD():
        if ClassD.__instance is None:
            ClassD.__instance = ClassD()
        return ClassD.__instance
