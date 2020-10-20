class CustomDate:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def updateDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def showDate(self):
        return "" + str(self.day) + "/" + str(self.month) + "/" + str(self.year)
