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
