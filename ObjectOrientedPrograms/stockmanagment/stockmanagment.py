class StockManagment:
    def __init__(self, stock_collection=[]):
        self.stock_collection = stock_collection

    def addstock(self, new_stock):
        self.stock_collection.append(new_stock)

    def deletestock(self, index):
        del self.stock_collection[index]

    def editstcok(self, index, edit_stock):
        self.stock_collection[index] = edit_stock

    def showAll(self):
        for stock in self.stock_collection:
            print(stock.to_dictionary())

    def PriceOfstock(self, index):
        stock_list = []
        for item in self.stock_collection:
            stock_list.append(item.to_dictionary())
        price = stock_list[index]['sharePrice'] / \
            stock_list[index]['numberOfShares']
        print(" stock{1} price of each share:{2}".format(index, price))

    def totalPriceOfstocks(self):
        total_price = 0
        stock_list = []
        for item in self.stock_collection:
            stock_list.append(item.to_dictionary())
        for index in range(len(stock_list)):
            total_price += stock_list[index]["sharePrice"]
        print("Total price of stocks:", total_price)

    def to_dict(self):
        stock_list = []
        for item in self.stock_collection:
            stock_list.append(item.to_dictionary())
        return {"Stocks": stock_list}
