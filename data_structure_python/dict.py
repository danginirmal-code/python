#Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
d = {i: i**2 for i in range(1, 11)}
print(d)

#Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
print(f"Value of key 5: {d[5]}")
print(f"Keys: {list((d.keys()))}")

#Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
d[11] = 121
d.pop(1)
print(d)

#Iterate over the dictionary created in Assignment 1 and print each key-value pair.
for key,value in d.items():
    print(f"key: {key},value:{value}")

#Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
cubes = {i: i**3 for i in range(1, 11)}
print(cubes)
#Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
d1 = {i: i**2 for i in range(1, 6)}
d2 = {i: i**2 for i in range(6, 11)}
d1.update(d2)
print(d1)

#Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.
student = {
    'name': 'John Doe',
    'age': 16,
    'grades': {
        'math': 90,
        'science': 85,
        'english': 88
    }
}
print(student)

multiples = {i: [i * j for j in range(1, 6)] for i in range(1, 6)}
print(multiples)

#Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
tuple_dict = {i: (i, i**2) for i in range(1, 6)}
print(tuple_dict)

#Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
d = {i: i**2 for i in range(1, 6)}
list_of_tuples = list(d.items())
print(list_of_tuples)


d = {i: i**2 for i in range(1, 11)}
even_dict = {k: v for k, v in d.items() if k % 2 == 0}
print(even_dict)

d = {i: i**2 for i in range(1, 6)}
swapped_dict = {v: k for k, v in d.items()}
print(swapped_dict)

#counting with dictionaries
def count_chars(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

string = "hello world"
print(count_chars(string))

#dictionaries to json
import json

book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960,
    'genre': 'Fiction'
}
book_json = json.dumps(book)
print(book_json)