from MiniComputer import MiniComputer


class Laptop(MiniComputer):
    __colour: str
    __model: str
    __generation: str

    def set_data(self):
        self.__colour = "Black"
