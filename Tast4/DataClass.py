class DataClass:
    __data1 = 0
    __data2 = 0
    __data3 = 0

    def set_fun1(self, val):
        self.__data1 = val
        self.set_fun2(val)

    def set_fun2(self, val):
        self.__data2 = val * val
        self.set_fun3(val)

    def set_fun3(self, val):
        self.__data3 = val * val * val

    def get_Data1(self):
        return self.__data1

    def get_Data2(self):
        return self.__data2

    def get_Data3(self):
        return self.__data3

    def print(self):
        print("Data 1:\t\t:" + str(self.get_Data1()) +
              "\nData 2:\t\t:" + str(self.get_Data2()) +
              "\nData 3:\t\t:" + str(self.get_Data3()) + ""
              )
