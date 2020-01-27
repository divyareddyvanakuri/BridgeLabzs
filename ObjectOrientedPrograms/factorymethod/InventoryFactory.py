class InventoryManagment:
    def __init__(self, rice_collection=[], wheat_collection=[], pulse_collection=[]):
        self.rice_collection = rice_collection
        self.wheat_collection = wheat_collection
        self.pulse_collection = pulse_collection

    def totalPriceOfInventory(self):
        pass


class RiceInventory(InventoryManagment):
    def totalPriceOfInventory(self):
        total_price = 0
        inventory_list = []
        for item in self.rice_collection:
            inventory_list.append(item.to_dictionary())
        for index in range(len(inventory_list)):
            total_price += inventory_list[index]["price"]
        return "price of inventory:{0}".format(total_price)


class WheatInventory(InventoryManagment):
    def totalPriceOfInventory(self):
        total_price = 0
        inventory_list = []
        for item in self.wheat_collection:
            inventory_list.append(item.to_dictionary())
        for index in range(len(inventory_list)):
            total_price += inventory_list[index]["price"]
        return "price of inventory:{0}".format(total_price)


class PulseInventory(InventoryManagment):
    def totalPriceOfInventory(self):
        total_price = 0
        inventory_list = []
        for item in self.pulse_collection:
            inventory_list.append(item.to_dictionary())
        for index in range(len(inventory_list)):
            total_price += inventory_list[index]["price"]
        return "price of inventory:{0}".format(total_price)


def factoryMethod(product_type):
    if product_type == 'rice':
        return RiceInventory()
    elif product_type == "wheat":
        return WheatInventory()
    elif product_type == "pulse":
        return PulseInventory()
    else:
        print("wrong")
