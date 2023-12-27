tuition=eval(input("please enter your tuition: "))
n=eval(input("please enter your year: "))
total_Tuition=0
while n<6 and n>=1:
    tuition*=1.07
    n-=1
    total_Tuition+=tuition
print(f"Your totalvTuition is{total_Tuition: .0f}")