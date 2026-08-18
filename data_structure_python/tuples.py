numbers=tuple([1,3,4,5,6,7,8])
print(numbers)

#tuple to list
# numbers=list((1,2,3,4,5,6))
# print(numbers)

mixed_tuple=(1,"Hello world",3.14,True)
print(mixed_tuple)

#accessing value tuple
print("accessing from 0 to 3rd index:",numbers[0:4])
print(numbers[::-1])
print("accessing last element:",numbers[-1])

concatenation=numbers+mixed_tuple
print(concatenation)
#count occarance
print(numbers.count(1))
#which number present in specific index
print(numbers.index(4))

tpl = tuple(range(1, 11))
print(tpl)

# printing first middle end element tuple
print(f"First element: {tpl[0]}")
print(f"Middle element: {tpl[len(tpl) // 2]}")
print(f"Last element: {tpl[-1]}")

#Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.

print(f"First three elements: {tpl[:3]}")
print(f"Last three elements: {tpl[-3:]}")
print(f"Elements from index 2 to 5: {tpl[2:6]}")
print(f"Print from the last  elements: {tpl[::-1]}")

#Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Matrix:")
for row in matrix:
    print(row)
print(f"Element at second row and third column: {matrix[1][2]}")

#concatinate 2 tuples
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
concatenated = tpl1 + tpl2
print(concatenated)

#occarance of element and index
tpl = (1, 2, 2, 3, 4, 4, 4, 5)
print(f"Occurrences of 4: {tpl.count(4)}")
print(f"Index of first occurrence of 2: {tpl.index(2)}")

#unpacking tuples
tpl = (1, 2, 3, 4, 5)
a, b, c, d, e = tpl
print(a, b, c, d, e)

#tuple conversion
lst = [1, 2, 3, 4, 5]
tpl = tuple(lst)
print(tpl)

#tuple of tuples
tpl_of_tpls = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(tpl_of_tpls)

#tuple and list
tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
lst.append(6)
tpl = tuple(lst)
print(tpl)

#tuple and string
string = "hello"
tpl = tuple(string)
joined_string = ''.join(tpl)
print(type(joined_string))


tpl_dict = {
    (1, 2): 3,
    (4, 5): 6,
    (7, 8): 9
}
print(tpl_dict[(1, 2)])

def min_in_tuple(tpl):
    return min(tpl)

def max_in_tuple(tpl):
    return max(tpl)

def sum_of_tuple(tpl):
    return sum(tpl)

sample_tpl = (1, 2, 3, 4, 5)
print(f"Minimum: {min_in_tuple(sample_tpl)}")
print(f"Maximum: {max_in_tuple(sample_tpl)}")
print(f"Sum: {sum_of_tuple(sample_tpl)}")