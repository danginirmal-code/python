


addition=lambda a,b:a+b
print(addition(2,4))

even_number=lambda num:num%2==0

print(even_number(4))

def addition(x,y,z):
    return x+y+z
print(addition(12,13,14))

#map
numbers=[1,2,3,4,5,6]
def square(number):
    return number**2
print(square(2))
print(list(map(lambda x:x**2,numbers)))