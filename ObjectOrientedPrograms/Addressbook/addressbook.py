from personcls import Person


class AddressBook:
    def __init__(self, collection=[]):
        self.collection = collection

    def getcollection(self):
        return self.collection

    def add_person(self, person):
        self.collection.append(person)


    def to_dict(self):
        person_dict_list = []
        for person_obj in self.collection:
            person_dict_list.append(person_obj.to_dictionary())
        return {'persons': person_dict_list}
