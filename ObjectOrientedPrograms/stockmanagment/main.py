from filesystem import FileSystem
from stockobjectclass import Stocks


def readStock():
    return{
        "shareName": input("enter share name:"),
        "numberOfShares": int(input("enter number of shares:")),
        "sharePrice": int(input("enter shares price:"))
    }


def addstock(stockmanagment_object):
    new_stock = Stocks(readStock())
    stockmanagment_object.addstock(new_stock)
    FileSystem().saveFile(stockmanagment_object)


def delete(stockmanagment_object):
    try:
        index = int(input("enter index:"))
        stockmanagment_object.deletestock(index)
    except IndexError as err:
        print("Handling Run-time error:", err)
    except ValueError as err:
        print("Handling Run-time error:", err)
    else:
        FileSystem().saveFile(stockmanagment_object)


def edit(stockmanagment_object):
    try:
        index = int(input("enter index:"))
        edit_stock = Stocks(readStock())
        stockmanagment_object.editstcok(index, edit_stock)
    except IndexError as err:
        print("Handling Run-time error:", err)
    except ValueError as err:
        print("Handling Run-time error:", err)
    else:
        FileSystem().saveFile(stockmanagment_object)


def printAll(stockmanagment_object):
    stockmanagment_object.showAll()


def priceOfshare(stockmanagment_object):
    stockmanagment_object.PriceOfstock()


def Totalpriceofstocks(stockmanagment_object):
    stockmanagment_object.totalPriceOfstocks()


while True:
    print("_____stockManagment Main-Menu_____")
    print(" 1.Add     2.Delete   3.Edit    4.ShowAll  5.priceOfEachShare    6.Totalpriceofstocks    7.Quit")
    try:
        choice = int(input("enter option:"))
    except ValueError as err:
        print("Handling Run-time error:", err)
    else:
        def switch_demo(choice):
            switcher = {
                1: addstock,
                2: delete,
                3: edit,
                4: printAll,
                5: priceOfshare,
                6: Totalpriceofstocks
            }
            return switcher.get(choice)
        if choice == 7:
            break
        func = switch_demo(choice)
        stockmanagment_object = FileSystem().readFile()
        try:
            print(func(stockmanagment_object))
        except TypeError as err:
            print("Handling Run-time error:", err)
