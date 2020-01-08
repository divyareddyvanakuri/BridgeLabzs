print("Temprature converter")
temprature = input("enter temprature value with units:")
temp = int(temprature[:-1])
units = temprature[-1]
if (units.lower()=='c') or (units.lower()=='f'):
    if (units.lower()=='c'):
        tempF = round((temp * 9/5)+32,3)
        print("temperature in fahrenheit {0}F".format(tempF))
    else:
        tempC = round((temp - 32)*5/9,3)
        print("temperature in Celsius {0}C".format(tempC))
else:
     print("please enter the temperature with valide units in fahrenheit or in Celsius eg:32F or 32C... ")
    