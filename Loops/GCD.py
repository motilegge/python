n1=eval(input("please input the first number: "))
n2=eval(input('please inpu the second number: '))
k=2
while k<=n1 and k<=n2:
    if n1%k==0 and n2%k==0:
        print(k)
    k+=1