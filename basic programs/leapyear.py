# Leap Year
def Leapyear(year):
    return ((year%4==0)and(year%100!=0)or(year%400==0))
year = int(input("enter year:"))
if len(str(year))<4:
    print("please enter four digited integer value")
else:
    Leapyear(year)
    if year == True:
        print("leap year")
    else:
        print("not a leap year")