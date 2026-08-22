import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape)

arr2=np.array([1,2,3,4,5])
arr2.reshape(1,5)
print(arr2)
print(arr2.shape)
#2d array
arr3=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr3.shape)

arr4=np.arange(0,10,2).reshape(5,1)
print(arr4)

one=np.ones((3,4))
print(one)

##indentity matric
print(np.eye(3))


arr=np.array([[1,2,3],[4,5,6]])
print("Array\n",arr)
print("shape",arr.shape)
print("Number of dimensions",arr.ndim)
print("size number of elements",arr.size)
print("Data type",arr.dtype)
print("Item size in bytes",arr.itemsize)

##numpy vectorized operation
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

### element wise addition
print("Addition",arr1+arr2)

##Element wise substraction
print("Substraction",arr1-arr2)

##element wise multipication
print("Multipication",arr1*arr2)
print(" Division",arr1/arr2)



#universal function
arr=np.array([2,3,4,5,6])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.log(arr))


#array slicing and indexing
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


print(arr[0][0])
print(arr[1:,2:])
print(arr[0:2,2:])

print(arr[1:,1:3])
print(arr)
print(arr[1:,0:2])

###statical concepts-Normalization
data=np.array([1,2,3,4,5,6,7,8,9,10])
mean=np.mean(data)
print("Mean",mean)
median=np.median(data)
print("Median",median)
std_dev=np.std(data)
print("Standard devication",std_dev)
variance=np.var(data)
print("Variance",variance)


#logical operation
data=np.array([1,2,3,4,5,6,7,8,9,10])
print(data[(data>5) & (data<=9)])