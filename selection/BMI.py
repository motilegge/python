weight=float(input("Please input weight: "))
height=float(input("please input height: "))
BMI = float(weight/(height**2))
if BMI<18.5:
    print("underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("normal")
else:
    print("overweight") 