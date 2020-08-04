class Bread:
    def __init__(self):
        self.__name = "Bread"
        self.__quantity = 0
        self.__price = 50

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
