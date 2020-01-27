class Rice:
    def __init__(self, d_rice={}):
        self.name = d_rice['name']
        self.weight = d_rice['weight']
        self.price = d_rice['price']

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getPrice(self):
        return self.price

    def to_dictionary(self):
        return{
            "name": self.name,
            "weight": self.weight,
            "price": self.price
        }


class Pulses:
    def __init__(self, d_pulses={}):
        self.name = d_pulses['name']
        self.weight = d_pulses['weight']
        self.price = d_pulses['price']

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getPrice(self):
        return self.price

    def to_dictionary(self):
        return{
            "name": self.name,
            "weight": self.weight,
            "price": self.price
        }


class Wheats:
    def __init__(self, d_wheats={}):
        self.name = d_wheats['name']
        self.weight = d_wheats['weight']
        self.price = d_wheats['price']

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getPrice(self):
        return self.price

    def to_dictionary(self):
        return{
            "name": self.name,
            "weight": self.weight,
            "price": self.price
        }
