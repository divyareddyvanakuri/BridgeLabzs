class Stocks:
    def __init__(self, stock={}):
        self.shareName = stock['shareName']
        self.numberOfShares = stock['numberOfShares']
        self.sharePrice = stock['sharePrice']

    def getShareName(self):
        return self.shareName

    def getNoOfShares(self):
        return self.numberOfShares

    def getSharePrice(self):
        return self.sharePrice

    def to_dictionary(self):
        return{
            "shareName": self.shareName,
            "numberOfShares": self.numberOfShares,
            "sharePrice": self.sharePrice
        }
