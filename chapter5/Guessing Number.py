import random
correctNumber = random.randint(0,101)
guessedNumber=0
while guessedNumber!=correctNumber:
    guessedNumber=eval(input("please guess the number: "))
    if guessedNumber<correctNumber:
        print("your number is lower: ")
    else:
        print("your number is higher: ")
print("you have got the  right number. the right number is", correctNumber)