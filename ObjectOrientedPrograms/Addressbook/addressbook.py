from personcls import Person


class AddressBook:
    def __init__(self, collection=[]):
        self.collection = collection

    def getcollection(self):
        return self.collection

    def add_person(self, person):
        self.collection.append(person)

    def removeperson(self, index):
        del self.collection[index]

    def updateperson(self, index, person):
        self.collection[index] = person

    def sortbyName(self):
        person_list=[]
        for person in self.collection:
            person_list.append(person.to_dictionary())
        print(sorted(person_list, key=lambda i: i['firstname']))
    
    def sortbyZipcode(self):
        person_list=[]
        for person in self.collection:
            person_list.append(person.to_dictionary())
        print(sorted(person_list, key=lambda i: i['zipcode']))
    
    def showAll(self):
        for person in self.collection:
            print(person.to_dictionary())

    def to_dict(self):
        person_dict_list = []
        for person_obj in self.collection:
            person_dict_list.append(person_obj.to_dictionary())
        return {'persons': person_dict_list}
