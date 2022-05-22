from random import randint
import numpy as np
#a = [ 2,1,3,4,5,6,7,2,2]
#arr = np.array(a)
#print(arr)


'''
a = [] 
n = int(input("Enter the size of array"))
for i in range(n):
    val = int(input("Enter your values"))
    a.append(val)
arr = np.array(a)

print(arr.ndim)
print(arr.shape)

'''
#arr = np.random.randint(1,2,4)
#print(arr)
'''
a = []
size = int(input("Enter your array size"))
for i in range (size):
    val = int(input("Enter you array"))
    a.append(val)
arr = np.array(a)
for i in range(arr.size):
    print(arr[i])
'''
'''
a = 1,2,3,4,5,6,7,8,9,10
arr = np.array(a)
print(arr)
x = np.asfarray(a)
x[::-1]
print(x)
'''
'''
a = 1,2,3,4,5,6,7,8,9
arr = np.array(a)
x = arr.reshape(3,3)
print(x)
'''
#arr = np.identity(3)
#print(arr)

r, c = map(int,input("Enter ").split())
l = []
l2 = []
for i in range(r):
    ele = list(map(int,input("Enter").split()))
    l.append(ele)
for i in range(r):
    ele = list(map(int,input("enter").split()))
    l2.append(ele)

A = np.array(l)
B = np.array(l2)
print(B)
arr = np.add(A,B)
arr1 = np.subtract(A,B)
arr2 = np.multiply(A,B)
arr3 = np.divide(A,B)
arr4 = np.power(A,B)
print("Add is = ",arr)
print("substraction is = ",arr1)
print("Multiplication is = ",arr2)
print("divide is = ",arr3)
print("Power is = ", arr4)
print(A%B)
'''
#arr = np.arange(1,100,2)
#x = np.all(95)
#print(x)
#print(arr)
'''
'''
a = []
b = int(input("Enter your size of array"))
for i in range(b):
    val = int(input("Enter your matrix size"))
    a.append(val)
print(a)
arr = np.array(a).reshape(2,2)
print(arr)

matrix = []
row = int(input("Enter no of rows"))
col = int(input("Enter no of columns"))
for i in range(row):
    a = []
    for j in range(col):
        val = int(input("Enter your values"))
        a.append(val)
        matrix.append(a)
arr = np.array(matrix)
for i in range(row):
    for j in range(col):
        print(arr[i][j],end=" ")
    print()
print(type(arr))
'''
