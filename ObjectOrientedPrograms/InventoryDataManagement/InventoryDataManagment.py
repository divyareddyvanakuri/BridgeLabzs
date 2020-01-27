from InventoryofRice import Rice
from InventoryofWheats import Wheats
from InventoryofPulses import Pulses


class InventoryDataManagment:
    def __init__(self, rice_collection=[], wheat_collection=[], pulse_collection=[]):
        self.rice_collection = rice_collection
        self.wheat_collection = wheat_collection
        self.pulse_collection = pulse_collection

    def addRice(self, rice):
        self.rice_collection.append(rice)

    def addWheat(self, wheat):
        self.wheat_collection.append(wheat)

    def addPulse(self, pulse):
        self.pulse_collection.append(pulse)

    def deleteRice(self, index):
        del self.rice_collection[index]

    def deleteWheat(self, index):
        del self.wheat_collection[index]

    def deletePulse(self, index):
        del self.pulse_collection[index]

    def editRice(self, index, rice):
        self.rice_collection[index] = rice

    def editWhear(self, index, wheat):
        self.wheat_collection[index] = wheat

    def editPulse(self, index, pulse):
        self.pulse_collection[index] = pulse

    def showRiceInventory(self):
        for rice in self.rice_collection:
            print(rice.to_dictionary())

    def showWheatInventory(self):
        for wheat in self.wheat_collection:
            print(wheat.to_dictionary())

    def showPulseInventory(self):
        for pulse in self.pulse_collection:
            print(pulse.to_dictionary())

    def totalPriceOfRiceInventory(self):
        total_price = 0
        rice_list = []
        for rice in self.rice_collection:
            rice_list.append(rice.to_dictionary())
        for index in range(len(rice_list)):
            total_price += rice_list[index]["price"]
        print("price of rice inventory:", total_price)

    def totalPriceOfWheatInventory(self):
        total_price = 0
        wheat_list = []
        for wheat in self.wheat_collection:
            wheat_list.append(wheat.to_dictionary())
        for index in range(len(wheat_list)):
            total_price += wheat_list[index]["price"]
        print("price of rice inventory:", total_price)

    def totalPriceOfPulseInventory(self):
        total_price = 0
        pulse_list = []
        for pulse in self.pulse_collection:
            pulse_list.append(pulse.to_dictionary())
        for index in range(len(pulse_list)):
            total_price += pulse_list[index]["price"]
        print("price of rice inventory:", total_price)

    def to_dict(self):
        rice_list = []
        wheat_list = []
        pulse_list = []
        for rice in self.rice_collection:
            rice_list.append(rice.to_dictionary())
        for wheat in self.wheat_collection:
            wheat_list.append(wheat.to_dictionary())
        for pulse in self.pulse_collection:
            pulse_list.append(pulse.to_dictionary())
        return {"Rice": rice_list, "Wheats": wheat_list, "Pulses": pulse_list}
