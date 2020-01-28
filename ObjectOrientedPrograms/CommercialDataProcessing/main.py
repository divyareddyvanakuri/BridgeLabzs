from filesystem import FileSystem
from datamanagment import Managment
from objectclass import Company, Share, Product


def read_company():
    return{
        "Name": input("enter company name:"),
        "Address": input("enter company address:")
    }


def read_share():
    return{
        "share": input("enter shares:"),
        "amount": int(input("enter amount:")),
        "stock": input("enter stock:"),
        "symbol": input("enter symbol:")
    }


def read_production():
    return{
        "product": input("enter product name:"),
        "count": int(input("enter production count:")),
        "productionDate": input("enter production date:"),
        "invesment": input("enter production invesment:")
    }


def addcompany(managment_object):
    new_company = Company(read_company())
    managment_object.addcompany(new_company)
    FileSystem().save_file(managment_object)


def removecompany(managment_object):
    name = input("enter company name:")
    managment_object.removecompany(name)
    FileSystem().save_file(managment_object)


def updatecompany(managment_object):
    name = input("enter company name:")
    edit_company = Company(read_company())
    managment_object.updatecompany(name, edit_company)
    FileSystem().save_file(managment_object)


def showAllCompanies(managment_object):
    managment_object.showcompany()


def addshare(managment_object):
    new_share = Share(read_share())
    managment_object.addshare(new_share)
    FileSystem().save_file(managment_object)


def removeshare(managment_object):
    share_name = input("enter share name:")
    managment_object.removeshare(share_name)
    FileSystem().save_file(managment_object)


def updateshare(managment_object):
    share_name = input("enter share name:")
    edit_share = Share(read_share())
    managment_object.updateshare(share_name, edit_share)
    FileSystem().save_file(managment_object)


def showAllshares(managment_object):
    managment_object.showshares()


def addproduct(managment_object):
    new_product = Product(read_production())
    managment_object.addproduct(new_product)
    FileSystem().save_file(managment_object)


def removeproduct(managment_object):
    product_name = input("enter product name:")
    managment_object.removeproduct(product_name)
    FileSystem().save_file(managment_object)


def updateproduct(managment_object):
    product_name = input("enter product name:")
    edit_product = Product(read_production())
    managment_object.updateproduct(product_name, edit_product)
    FileSystem().save_file(managment_object)


def showAllproducts(managment_object):
    managment_object.showproduct()


while True:

    print("___commerialDataManagment main menu___")
    print(" 1.Managecompanycontact")
    print(" 2.Managecompanyshare"), print(
        " 3.Managecompanyproduction"), print(" 4.Quitprogram")
    try:
        option = int(input("enter option:"))
    except ValueError as err:
        print("run time err:", err)
    else:
        if option == 1:
            print("___Submenu___"), print(" 1.add"), print(
                " 2.delete"), print(" 3.edit"), print(" 4.showall")
            try:
                choice = int(input("Enter choice 1-4:"))
            except ValueError as err:
                print("Handling Run-time error:", err)
            except NameError as err:
                print("Handling Run-time error:", err)
            else:
                def switch_demo(choice):
                    switcher = {
                        1: addcompany,
                        2: removecompany,
                        3: updatecompany,
                        4: showAllCompanies
                    }
                    return switcher.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
                func = switch_demo(choice)
                managment_object = FileSystem().read_file()
                print(func(managment_object))

        elif option == 2:
            print("___Submenu___"), print(" 1.add"), print(
                " 2.delete"), print(" 3.edit"), print(" 4.showall")
            try:
                choice = int(input("Enter choice 1-4:"))
            except ValueError as err:
                print("Handling Run-time error:", err)
            except NameError as err:
                print("Handling Run-time error:", err)
            else:
                def switch_demo(choice):
                    switcher = {
                        1: addshare,
                        2: removeshare,
                        3: updateshare,
                        4: showAllshares
                    }
                    return switcher.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
                func = switch_demo(choice)
                managment_object = FileSystem().read_file()
                print(func(managment_object))
        elif option == 3:
            print("___Submenu___"), print(" 1.add"), print(
                " 2.delete"), print(" 3.edit"), print(" 4.showall")
            try:
                choice = int(input("Enter choice 1-4:"))
            except ValueError as err:
                print("Handling Run-time error:", err)
            except NameError as err:
                print("Handling Run-time error:", err)
            else:
                def switch_demo(choice):
                    switcher = {
                        1: addproduct,
                        2: removeproduct,
                        3: updateproduct,
                        4: showAllproducts
                    }
                    return switcher.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
                managment_object = FileSystem().read_file()
                print(func(managment_object))
        elif option == 4:
            break
        else:
            print("invalid choice")
