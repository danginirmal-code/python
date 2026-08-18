
#Create a list of the first 20 positive integers. Print the list.
lst=list(range(1,21))
print(lst)
#Print the first, middle, and last elements of the list created in Assignment 1.
print(f"first element {lst[0]}")
print(f"Middle element: {lst[len(lst) // 2]}")
print(f"Last element: {lst[-1]}")
print(f"First five element {lst[:5]}")
print(f"Last five element {lst[-5:]}")
print(f" element from 5 to 15 {lst[5:16]}")

squares=[x**2 for x in lst]
print(squares)
evens=[x for x in lst if x%2==0]
print(evens)

import random
random_numbers=[random.randint(1, 20) for _ in range(15)]
print(f"Original list: {random_numbers}")
sorted_numbers = sorted(random_numbers)
print(f"Sorted in ascending order: {sorted_numbers}")
sorted_numbers_desc = sorted(random_numbers, reverse=True)
print(f"Sorted in descending order: {sorted_numbers_desc}")
unique_numbers = list(set(random_numbers))
print(f"List with duplicates removed: {unique_numbers}")

##nested list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
for row in matrix:
    print(row)
print(f" Second row and third column:{matrix[1][2]}")

##list of dictionaries

students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 72},
    {'name': 'Charlie', 'score': 95},
    {'name': 'David', 'score': 65},
    {'name': 'Eve', 'score': 78}
]
sorted_students=sorted(students,key=lambda x:x['score'],reverse=True)
print("Sorted students by score in descending order:")
for student in sorted_students:
    print(student)

## Transpose matrix
def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)

for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)

def flatten_list(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = flatten_list(nested_list)
print("Original nested list:")
print(nested_list)
print("Flattened list:")
print(flattened)

##list manipulation

lst = list(range(1, 11))
print(f"Original list: {lst}")
del lst[6]
del lst[4]
del lst[2]
lst.insert(5, 99)
print(f"Modified list: {lst}")

#converting list into list of  tuple
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = list(zip(list1, list2))
print(zipped)

#Reverse list
def reverse_list(lst):
    return lst[::-1]

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")

# rotate lis by n position
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list, 2)
print(f"Original list: {original_list}")
print(f"Rotated list: {rotated_list}")
#
#list intersection
def list_intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list_intersection(list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection}")