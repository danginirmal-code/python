#find the number is positive or not 
number=float(input("Enter a number:"))
if number>=0:
    print("Number is positve")
else:
    print("Number is negative")

#find the number is positive or not also 0 or not
number=float(input("Enter a number:"))
if number>0:
    print("Number is positve")
elif number<0:
    print("Number is negative")
else:
    print("Number is zero")

#find about the number 

number = float(input("Enter a number: "))
if number >0:
    if number%2==0:
        print("Number is positive and odd")
    else:
        print("Number is positive and even")
else:
    print("Number is negative")

for i in range(1,11):
    print(i)
i=1
while(i<=10):
    print(i)
    i+=1
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
total=0
while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
            break
    total += number
print(f"The sum of all the numbers is {total}.")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)


#Write a program that calculates the factorial of a number input by the user using a while loop
number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is {factorial}.")


#Write a program that calculates the sum of the digits of a number input by the user using a while loop.

number=int(input("Enter a number:"))
sum_of_digit=0
while number > 0:
    digit=number%10
    sum_of_digit+=digit
    number=number//10
print(f"The sum of digit is {sum_of_digit}")

n = int(input("Enter the number of Fibonacci numbers to print: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1
