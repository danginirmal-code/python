age=20
if age>=18:
    print("You are allowed to vote in the election")
##if else statement
age=16
if age >=18:
    print("You are eligible for voting")
else:
    print("You are a minor")

##elseif  condition
age=20
if age<18:
    print("You are a minor")
elif age <10:
    print("You are a teenager")
else:
    print("You are an adult")

#nested conditional statement
num=int(input("Enter the Number"))
if num >=0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")

##leap year
year=int(input("Enter the year"))
if year%4==0:
    if year%100==0:
        if(year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")

