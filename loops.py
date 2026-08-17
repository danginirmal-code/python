##for loop

for i in range(5):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(10,1,-2):
    print(i)
str="Nirmal Dangi"
for i in str:
    print(i)
##while loop
##the while loop continues to execute as long as condition is true
count=0
while count < 5:
    print(count)
    count=count+1
## break statement
for i in range(10):
    if i==5:
        break
    print(i)
##continue
#skips current statement and goes to next
for i in range(10):
    if i%2==0:
        continue
    print(i)
#pass operator
for i in range(5):
    if i==3:
        pass
    print(i)
for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")

##calculate the sum of first natuaral number 
n=10
sum=0
count=1
while count<=n:
    sum=sum+count
    count=count+1
print("Sum of first 10 natual number",sum)

##prime number between 1 and 100

for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
