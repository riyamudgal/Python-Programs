'''Write a day in you life when you feel it is the best day of life and calculate the corresponding day of the week for any particular date in the past or future.

The first line of each test case or query contains the three space-separated integers denoting the 'Day', 'Month', and the 'Year' respectively.

The answer will be one of the following values  "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday".

SAMPLE INPUT 
29 2 1920

SAMPLE OUTPUT 
Sunday
'''

import datetime
import calendar

def day(d,m,y):
    t=[0,3,2,5,0,3,5,1,4,6,2,4]
    y-=m < 3
    return ((y+int(y/4) - int(y/100) + int(y/400) + t[m-1]+d) %7)

d=int(input())
m=int(input())
y=int(input())
d=day(d,m,y)

if d==1:
    print("Monday")
elif d==2:
    print("Tuesday")
elif d==3:
    print("Wednesday")
elif d==4:
    print("Thursday")
elif d==5:
    print("Friday")
elif d==6:
    print("Saturday")
else:
    print("Sunday")

