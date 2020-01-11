#print("Temprature conversion main-menu:")
#print(" 1-convert from celsius to fahranheit")
#print(" 2-convert form fahranheit to celsius")
#option = int(input("choose an option 1 or 2:"))
#class tconversion:
    #def __init__(self,temprature):
        #self.temprature = temprature
def fcon(temprature):
    return int((temprature * 9/5)+32)
def ccon(temprature):
    return int((temprature - 32)*5/9)
'''if option == 1:
    t = tconversion(int(input("enter temprature value:")))
    print("Temprature:",t.fcon(),"degrees fahranheit")
elif option==2:
    t = tconversion(int(input("enter temprature value:")))
    print("Temprature:",t.ccon(),"degrees celsius")
else:
    print("please enter choose in between 1 or 2")'''
