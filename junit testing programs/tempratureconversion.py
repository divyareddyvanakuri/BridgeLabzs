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
t = tconversion(34)
if option == 1:
    print("convert from celsius to fahranheit:",t.fcon())
else:
    print("convert form fahranheit to celsius:",t.ccon())