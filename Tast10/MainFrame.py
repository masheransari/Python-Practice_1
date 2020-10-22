from Computer import Computer


class MainFrame(Computer):
    __cost: float
    name: str

    def __init__(self, cost, name):
        self.__cost = cost
        self.name = name

    def billing(self):
        return "Override method in MainFrame Class"
