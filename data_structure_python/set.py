s = set(range(1, 11))
print(s)
s.add(11)
s.remove(1)
print(s)


#set operations
set1 = set(range(1, 6))
set2 = set(range(2, 11, 2))
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")



squares = {x**2 for x in range(1, 11)}
print(squares)

evens = {x for x in s if x % 2 == 0}
print(evens)

#create a set with dublicate element and remove the single element
s = {1, 2, 2, 3, 4, 4, 5}
unique_s = set(s)
print(unique_s)


set1 = set(range(1, 6))
set2 = set(range(1, 4))
print(f"Is set2 a subset of set1? {set2.issubset(set1)}")
print(f"Is set1 a superset of set2? {set1.issuperset(set2)}")


fs = frozenset(range(1, 6))
print(fs)



s = set(range(1, 6))
lst = list(s)
lst.append(6)
s = set(lst)
print(s)


d = {
    frozenset({1, 2}): 3,
    frozenset({3, 4}): 7,
    frozenset({5, 6}): 11
}
print(d)

#iterating over set
s = set(range(1, 6))
for elem in s:
    print(elem)

#removing element from set
s = set(range(1, 6))
while s:
    s.pop()
    print(s)

#Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)

#test if certain element present in the set 
s = set(range(1, 6))
print(3 in s)
print(6 in s)

#set containing tuples

s = { (1, 2), (3, 4), (5, 6) }
print(s)