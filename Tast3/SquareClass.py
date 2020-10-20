class SquareClass:
    def __init__(self):
        self.data1 = 0.0
        self.data2 = 0.0

    def get_data(self, value):
        self.data1 = value
        self.data2 = value * value

    def showData(self):
        print("Data1: " + str(self.data1))
        print("Squared Dated: " + str(self.data2))
