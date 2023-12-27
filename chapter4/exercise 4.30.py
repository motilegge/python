weight=eval(input("Please input your weight: "))
height=eval(input("Please input your height: "))
if ((weight>50 or height>160)  and not  (weight>50 and height>160)):
    print(True)
else:
    print(False)