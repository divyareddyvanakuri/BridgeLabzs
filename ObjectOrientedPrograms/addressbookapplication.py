from addressbook import AddressBook
from filesystem import Filesystem
from personcls import Person
myfile = Filesystem()
# mybook = AddressBook()

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
    myfile.saveFile("/home/user/Desktop/programming/ObjectOrientedPrograms/addressbookfile.json", addressbook)


def updatePerson():
    return "two"


def removePerson():
    pass


def sortByName():
    pass


def sortByZipCode():
    pass


def printAll():
    pass


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
            pass

        elif option == 2:
            addressbook_object = myfile.readFile()
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
                        1: addPerson(addressbook_object),
                        2: updatePerson(),
                        3: removePerson(),
                        4: sortByName(),
                        5: sortByZipCode(),
                        6: printAll()
                    }
                    return switcher.get(choice, lambda: "invalide choice,Ensure option will be 1-6")
                func = switch_demo(choice)
                

        elif option == 3:
            break

        else:
            print("Inavlide option,Ensure option will be 1-3")
