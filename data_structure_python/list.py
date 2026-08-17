lst=[]
print(type(lst))

names=["Nirmal","Jack","Jacob",1,2,3,4,5]
print(names)

mixed_list=[1,"Hello","3.14",True]
print(mixed_list)

##accessing list elements
fruits=["apple","banana","cherry","kiwi"]
print(fruits[1:])
fruits[1]="watermelon"
print(fruits)
##list methonds
fruits.append("Orange")
print(fruits)
fruits.insert(1,"dragonfruit")
print(fruits)
fruits.remove("apple")
print(fruits)
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

##slicing list
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])
for number in numbers:
    print(number)
for index,number in enumerate(numbers):
    print(index,number)

##list comprehension
lst=[]
for x in range(10):
    lst.append(x**2)
print(lst)

print([x**2 for x in range(10)])

##list comprehension with condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)
print(lst)
even_number=[num for num in range(10) if num%2==0]
print(even_number)

#nested list comphrension
lst1=[1,2,3,4]
lst2=['a','b','c','d']
pair=[[i,j] for i in lst1 for j in lst2]
print(pair)
words=["hello","world"]
length=[len(word) for word in words]
print(length)