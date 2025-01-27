import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# matrix A

A = np.array([[1,2,3],
              [0,1,6],
              [5,6,0]])

# inverse of a
A_inv = np.linalg.inv(A)

identity1 = np.dot(A, A_inv)
identity2 = np.dot(A_inv, A)


print('Matrix A:')
print(A)

print('Inverse of Matrix A: ')
print(A_inv)

print('\nA * A_inv: ')
print(identity1)

print('\nA_inv * A: ')
print(identity2)