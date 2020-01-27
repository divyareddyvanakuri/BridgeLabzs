from addressbook import AddressBook
from filesystem import Filesystem
from personcls import Person
file_object = Filesystem()

def read_person():
    return {
        'firstname': input("enter firstname:"),
        'lastname': input("enter lastname:"),
        'address': input("enter address:"),
        'city': input("enter city:"),
        'state': input("enter state:"),
        'zipcode': input("enter zipcode:"),
        'phonenumber': input("enter phonemuber:")
    }
def addPerson(addressbook):
    new_person = Person(read_person())
    addressbook.add_person(new_person)
    file_object.saveFile("addressbookfile.json", addressbook)

def updatePerson(addressbook):
    index = int(input("enter index value:"))
    update_person = Person(read_person())
    addressbook.updateperson(index, update_person)
    file_object.saveFile("addressbookfile.json", addressbook)

def removePerson(addressbook):
    index = int(input("enter index value:"))
    addressbook.removeperson(index)
    file_object.saveFile("addressbookfile.json", addressbook)

def sortByName(addressbook):
    addressbook.sortbyName()

def sortByZipCode(addressbook):
    addressbook.sortbyZipcode()

def printAll(addressbook):
    addressbook.showAll()


print("Address Book Main-menu:")
print(" 1.create New Address Book"), print(
    " 2.open Existing Address Book"), print(" 3.Quitprogram")


while True:
    try:
        option = int(input("Enter option 1-3:"))
    except ValueError as err:
        print("Handling Run-time error:", err)
    except NameError as err:
        print("Handling Run-time error:", err)
    else:
        if option == 1:
            addressbook_object = file_object.readFile()
            new_file_name = input("enter new file name")
            file_object.saveFile(new_file_name+".json",addressbook_object)

        elif option == 2:
            addressbook_object = file_object.readFile()
            print(" 1.Add a person"), print(
                " 2.Edit a person"), print(" 3.Delete a person")
            print(" 4.sort Entries by Name"), print(
                " 5.sort Entries by Zip"), print(" 6.print AllEntries")

            try:
                choice = int(input("Enter choice 1-6:"))
            except ValueError as err:
                print("Handling Run-time error:", err)
            except NameError as err:
                print("Handling Run-time error:", err)
            else:
                def switch_demo(choice):
                    switcher = {
                        1: addPerson,
                        2: updatePerson,
                        3: removePerson,
                        4: sortByName,
                        5: sortByZipCode,
                        6: printAll
                    }
                    return switcher.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
                func = switch_demo(choice)
                print(func(addressbook_object))

        elif option == 3:
            break

        else:
            print("Inavlide option,Ensure option will be 1-3")
