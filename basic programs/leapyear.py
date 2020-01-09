# Leap Year
def Leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False 
year = int(input("enter year:"))
if len(str(year))<4:
    print("please enter four digited integer value")
else:
    if Leapyear(year) == True:
        print("leap year")
    else:
        print("not a leap year")