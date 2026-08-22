def square(n):
    for i in range(n):
        yield i**2

a=square(3)
print(next(a))
print(next(a))
for i in square(3):
    print(i)


def my_generator():
    yield 1
    yield 2
    yield 3
gen=my_generator()
for value in gen:
    print(value)

def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line
file_path="large_file.txt"
for line in read_large_file(file_path):
    print(line.strip())