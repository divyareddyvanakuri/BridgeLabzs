from InventoryofRice import Rice
from InventoryofWheats import Wheats
from InventoryofPulses import Pulses
from filesystem import FileSystem
from InventoryDataManagment import InventoryDataManagment
def readRice():
    return{
        "name":input("enter type of the rice name:"),
        "weight":int(input("enter weight:")),
        "price": int(input("enter price per kg:"))
    }
def readWheats():
    return{
        "name":input("enter type of the rice name:"),
        "weight":int(input("enter weight:")),
        "price":int(input("enter price per kg:"))
    }
def readPulses():
    return{
        "name":input("enter type of the rice name:"),
        "weight":int(input("enter weight:")),
        "price":int(input("enter price per kg:"))
    }
def addRice(data_object):
    new_rice = Rice(readRice())
    data_object.addRice(new_rice)
    FileSystem().saveFile(data_object)
def removeRice(data_object):
    index = int(input("enter index value:"))
    data_object.deleteRice(index)
    FileSystem().saveFile(data_object)
def updateRice(data_object):
    index = int(input("enter index value:"))
    edit_rice = Rice(readRice())
    data_object.editRice(index,edit_rice)
    FileSystem().saveFile(data_object)
def totalPriceOfRiceInventory(data_object):
    data_object.totalPriceOfRiceInventory()
def printRiceInventory(data_object):
    data_object.showRiceInventory()
def addWheat(data_object):
    new_wheat = Wheats(readWheats())
    data_object.addWheat(new_wheat)
    FileSystem().saveFile(data_object)
def removeWheat(data_object):
    index = int(input("enter index value:"))
    data_object.deleteWheat(index)
    FileSystem().saveFile(data_object)
def updateWheat(data_object):
    index = int(input("enter index value:"))
    edit_wheat = Wheats(readWheats())
    data_object.editWheat(index,edit_wheat)
    FileSystem().saveFile(data_object)
def totalPriceOfWheatInventory(data_object):
    data_object.totalPriceOfWheatInventory()
def printWheatInventory(data_object):
    data_object.showWheatInventory()
def addPulse(data_object):
    new_pulse = Pulses(readPulses())
    data_object.addPulse(new_pulse)
    FileSystem().saveFile(data_object)
def removePulse(data_object):
    index = int(input("enter index value:"))
    data_object.deletePluse(index)
    FileSystem().saveFile(data_object)
def updatePulse(data_object):
    index = int(input("enter index value:"))
    edit_pulse = Pulses(readPulses())
    data_object.editPulse(index,edit_pulse)
    FileSystem().saveFile(data_object)
def totalPriceOfPulseInventory(data_object):
    data_object.totalPriceOfPulseInventory()
def printPulseInventory(data_object):
    data_object.showPulseInventory()
while True:
    print("Inventory Main-menu:")
    print(" 1.Manage Inventory of rice"),print(" 2. Manage Inventory of wheat")
    print(" 3.Manage Inventory of pulse"),print(" 4.show All"),print(" 5.Quitprogram")
    try:
        option = int(input("enter Inventory:"))
    except ValueError as err:
        print("Handling Run-time error:", err)
    else:
        if option == 1:
            print("sub menu")            
            print(" 1.Add"),print(" 2.Delete"),print(" 3.update"),print(" 4.Total price of Inventory")
            print(" 5.show All")
            
            def switch_demo1(choice):
                switcher1 = {
                    1: addRice,
                    2: removeRice,
                    3: updateRice,
                    4: totalPriceOfRiceInventory,
                    5: printRiceInventory
                }
                return switcher1.get(choice, lambda: "invalide choice,Ensure option will be 1-5")
            try:
                choice = int(input("Operations of inventory:"))
            except ValueError as err:
                 print("Handling Run-time error:", err)
            else:
                func1 = switch_demo1(choice)
                data_object=FileSystem().readFile()
                print(func1(data_object))
        elif option == 2:
            print("sub menu")
            print(" 1.Add"),print(" 2.Delete"),print(" 3.update"),print(" 4.Total price of Inventory")
            print(" 5.show All")
            
            def switch_demo2(choice):
                switcher2 = {
                    1: addWheat,
                    2: removeWheat,
                    3: updateWheat,
                    4: totalPriceOfWheatInventory,
                    5: printWheatInventory
                }
                return switcher2.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
            try:
                choice = int(input("Operations of inventory:"))
            except ValueError as err:
                 print("Handling Run-time error:", err)
            else:
                func2 = switch_demo2(choice)
                data_object=FileSystem().readFile()
                print(func2(data_object))
        elif option == 3:
            print("sub menu")
            print(" 1.Add"),print(" 2.Delete"),print(" 3.update"),print(" 4.Total price of Inventory")
            print(" 5.show All")
            def switch_demo3(choice):
                switcher3 = {
                    1: addPulse,
                    2: removePulse,
                    3: updatePulse,
                    4: totalPriceOfPulseInventory,
                    5: printPulseInventory
                }
                return switcher3.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
            try:
                choice = int(input("Operations of inventory:"))
            except ValueError as err:
                 print("Handling Run-time error:", err)
            else:
                func3 = switch_demo3(choice)
                data_object=FileSystem().readFile()
                print(func3(data_object))
        elif option == 4:
            pass
        elif option == 5:
            break
        else:
            print("wrong choice")