year=eval(input("please inout the Calendar year: "))
if (year%4==0 and year%100!=0) or (year%4==0 and year%400==0):
    print("It is Leap is Leap Year")
else:
    print("It is not a leap Year")
