import random


class Data:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.data1 = random.randint(0, 10)

    def getdataFromUser(self):
        self.data2 = int(input("Enter any number: "))

    def showdata(self):
        printData = "The value of data1 = " + str(self.data1) + " & data2 = " + str(self.data2)
        print(printData)
