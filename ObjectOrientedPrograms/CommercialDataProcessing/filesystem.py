import json
from objectclass import Company,Share,Product
from datamanagment import Managment

class FileSystem:
    def read_file(self):
        company_list=[]
        share_list=[]
        product_list=[]
        with open("commerialdata.json","r") as readFile:
            data = json.load(readFile)
        for company in data['Company']:
            company_list.append(Company(company))
        for share in data['Shares']:
            share_list.append(Share(share))
        for product in data['Products']:
            product_list.append(Product(product))
        managment_object = Managment(company_list,share_list,product_list)
        return managment_object
    def save_file(self,managment_object):
        with open("commerialdata.json","w") as saveFile:
            json.dump(managment_object,saveFile)
