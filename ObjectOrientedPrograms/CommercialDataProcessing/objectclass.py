class Company:
    def __init__(self, c_dict={}):
        self.Name = c_dict['Name']
        self.Address = c_dict['Address']

    def getName(self):
        return self.Name

    def getAddress(self):
        return self.Address

    def to_company_dictionary(self):
        return{
            "Name": self.Name,
            "Address": self.Address
        }


class Share:
    def __init__(self, s_dict={}):
        self.share = s_dict['share']
        self.amount = s_dict['amount']
        self.stock = s_dict['stock']
        self.symbol = s_dict['symbol']

    def getShare(self):
        return self.share

    def getAmount(self):
        return self.amount

    def getStock(self):
        return self.stock

    def getSymbol(self):
        return self.symbol

    def to_share_dictionary(self):
        return{
            "share": self.share,
            "amount": self.amount,
            "stock": self.stock,
            "symbol": self.symbol
        }


class Product:
    def __init__(self, p_dict={}):
        self.product = p_dict['product']
        self.count = p_dict['count']
        self.productionDate = p_dict['productionDate']
        self.invesment = p_dict['invesment']

    def getProduct(self):
        return self.product

    def getCount(self):
        return self.count

    def getProduction(self):
        return self.productionDate

    def getInvesment(self):
        return self.invesment

    def to_product_dictionary(self):
        return{
            "product": self.product,
            "count": self.count,
            "productionDate": self.productionDate,
            "invesment": self.invesment
        }
