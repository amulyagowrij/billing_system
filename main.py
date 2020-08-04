import sys

from bread import Bread
from chocolate import Chocolate
from exit import Exit
from milk import Milk






if __name__ == "__main__":
    itemList = [Milk(), Chocolate(), Bread(), Exit()]

    print("Item available")
    counter = 1
    for element in itemList:
        print(str(counter) + "." + element.get_name())
        counter = counter + 1

    while True:
        item = int(input("Enter the items you want"))
        if item == 4:
            print("thankyou for shopping with us")
            print("items in the basket:")
            for element in itemList:
                if element.get_name() != "Exit" and element.get_quantity() > 0:
                    print(element.get_name(),element.get_quantity())


            print("Total bill:")
            billAmount = 0
            for element in itemList:
                if element.get_name() != "Exit":
                 billAmount = billAmount + element.get_quantity() * element.get_price()
            print(billAmount)
            sys.exit()

        quantity = int(input("Enter the quantity"))
        itemList[item - 1].set_quantity(quantity)
        print("item: {}  quantity: {}  added to the basket".format(itemList[item - 1].get_name(),
                                                                   itemList[item - 1].get_quantity()))
