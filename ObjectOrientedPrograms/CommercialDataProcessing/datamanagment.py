from objectclass import Company, Share, Product


class Managment:
    def __init__(self, company_collection=[], share_collection=[], product_collection=[]):
        self.company_collection = company_collection
        self.share_collection = share_collection
        self.product_collection = product_collection

    def addcompany(self, company):
        self.company_collection.append(company)

    def removecompany(self, name):
        c_list = []
        for company in self.company_collection:
            c_list.append(company)
        for index in range(len(c_list)):
            if c_list[index]['Name'] == name:
                del self.company_collection[index]

    def updatecompany(self, name, company):
        c_list = []
        for company in self.company_collection:
            c_list.append(company)
        for index in range(len(c_list)):
            if c_list[index]['Name'] == name:
                self.company_collection[index] = company

    def showcompany(self):
        for company in self.company_collection:
            print(company.to_company_dictionary())

    def addshare(self, share):
        self.share_collection.append(share)

    def removeshare(self, share_name):
        s_list = []
        for share in self.share_collection:
            s_list.append(share)
        for index in range(len(s_list)):
            if s_list[index]['share'] == share_name:
                del self.share_collection[index]

    def updateshare(self, share_name, share):
        s_list = []
        for share in self.share_collection:
            s_list.append(share)
        for index in range(len(s_list)):
            if s_list[index]['share'] == share_name:
                self.share_collection[index] = share

    def showshares(self):
        for share in self.share_collection:
            print(share.to_share_dictionary())

    def addproduct(self, product):
        self.product_collection.append(product)

    def removeproduct(self, product_name):
        p_list = []
        for product in self.product_collection:
            p_list.append(product)
        for index in range(len(p_list)):
            if p_list[index]['product'] == product_name:
                del self.product_collection[index]

    def updateproduct(self, product_name, share):
        s_list = []
        for share in self.share_collection:
            s_list.append(share)
        for index in range(len(s_list)):
            if s_list[index]['product'] == product_name:
                self.share_collection[index] = share

    def showproduct(self):
        for share in self.share_collection:
            print(share.to_share_dictionary())

    def to_dict(self):
        c_list = []
        s_list = []
        p_list = []
        for company in self.company_collection:
            c_list.append(company.to_company_dictionary())
        for share in self.share_collection:
            s_list.append(share.to_share_dictionary())
        for product in self.product_collection:
            p_list.append(product.to_product_dictionary())
        return {"Company": c_list, "Shares": s_list, "Products": p_list}
