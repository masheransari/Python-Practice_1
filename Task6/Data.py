class Data:
    counter = 0

    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        Data.counter += 1

    def printcount(self):
        print("The number of objects created were "+str(Data.counter))
