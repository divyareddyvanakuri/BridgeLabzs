print("Temprature conversion main-menu")
print("1-convert from celsius to fahranheit")
print("2-convert form fahranheit to celsius")
option = int(input("choose an option 1 or 2:"))
class tconversion:
    def __init__(self,temprature):
        self.temprature = temprature
    def fcon(self):
        return round((self.temprature * 9/5)+32,3)
    def ccon(self):
        return round((self.temprature - 32)*5/9,3)
t = tconversion(int(input("enter temprature value:")))
if option == 1:
    print("Temprature:",t.fcon(),"degrees fahranheit")
else:
    print("Temprature:",t.ccon(),"degrees celsius")