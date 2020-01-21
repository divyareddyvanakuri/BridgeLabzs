import calendar
year = 2020
month = 2
day = 1
dayNumber = calendar.weekday(year, month, day) 
days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
print(days[dayNumber])
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
noofdays = [31,28,31,30,31,30,31,31,30,31,30,31]

month_index= months.index(month)
noofday = noofdays[month_index]
calendar_2D=[[days],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "] ]
z = 1
k = 1
Found = False
while k!=6 and not Found:
    number = z
    for i in range(dayNumber,7):
        if number<=noofday:
            calendar_2D[k][i]=number
        else:
            Found = True
        number += 1
    dayNumber = 0
    z = number
    k += 1
print("calendar of {0} {1} : {2}".format(month,year,calendar_2D))