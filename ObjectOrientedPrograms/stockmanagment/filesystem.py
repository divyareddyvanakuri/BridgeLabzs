import json
from stockobjectclass import Stocks
from stockmanagment import StockManagment


class FileSystem:
    def readFile(self):
        stock_list = []
        with open("stock.json", "r") as read_file:
            data = json.load(read_file)
        for stock in data['Stocks']:
            stock_list.append(Stocks(stock))
        stcokmanagment_object = StockManagment(stock_list)
        return stcokmanagment_object

    def saveFile(self, stcokmanagment_object):
        with open("stock.json", "w") as save_file:
            json.dump(stcokmanagment_object.to_dict(), save_file, indent=2)
