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
