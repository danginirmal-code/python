my_list=[1,2,3,4,5,6]
for i in my_list:
    print(i)
iterator=iter(my_list)
try:
    next(iterator)
except StopIteration:
    print("There are no elements in Iterator")
print(next(iterator))
print(next(iterator))