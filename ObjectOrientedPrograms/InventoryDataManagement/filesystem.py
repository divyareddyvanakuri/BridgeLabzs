import json
from InventoryofRice import Rice
from InventoryofWheats import Wheats
from InventoryofPulses import Pulses
from InventoryDataManagment import InventoryDataManagment


class FileSystem:
    def readFile(self):
        rice_list = []
        wheat_list = []
        pulse_list = []
        with open("inventoryfile.json", "r") as read_file:
            data = json.load(read_file)

        for rice in data['Rice']:
            rice_list.append(Rice(rice))

        for wheat in data['Wheats']:
            wheat_list.append(Wheats(wheat))

        for pulse in data['Pulses']:
            pulse_list.append(Pulses(pulse))

        dataManagment_object = InventoryDataManagment(
            rice_list, wheat_list, pulse_list)

        return dataManagment_object

    def saveFile(self, dataManagment_object):
        with open("inventoryfile.json", "w") as save_file:
            json.dump(dataManagment_object.to_dict(), save_file, indent=2)

