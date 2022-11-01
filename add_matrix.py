#python -m pip install -U pip setuptools
import numpy as np 
#creating first matrix
A = np.array([1,2], [3,4])
#creating second matrix
B = np.array([[4,5], [6,7]])
print("Printing elements of first matrix")
print(A)
print("printing elements of second matrix")
print(B)
#adding two matrix
print("Addition of two matrix")
print(np.add(A, B))