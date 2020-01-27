import json
from personcls import Person
from addressbook import AddressBook

class Filesystem:

    def readFile(self):
        persons = []
        with open('addressbookfile.json', 'r') as read_file:
            data = json.load(read_file)
        for person_dict in data['persons']:
            person_object = Person(person_dict)
            persons.append(person_object)
        addressbook = AddressBook(persons)
        return addressbook

    def saveFile(self, filename, addressbook):
        with open(filename, "w") as f:
            json.dump(addressbook.to_dict(), f, indent=2)



