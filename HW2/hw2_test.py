import matplotlib.pyplot as plt
import sympy
import numpy as np
import sys

actual_basis_vec1 = np.array([1,0,0])
actual_basis_vec2 = np.array([0,1, 0])
actual_basis_vec3 = np.array([0,0,1])
new_basis_vec1 =  np.array([2,3, 4])
new_basis_vec2 = np.array([-1,1, 1])
new_basis_vec3 = np.array([-1,0, 1])
vec_old = np.array([[2],[-4],[2]])

new_basis = np.transpose(np.array([new_basis_vec1, new_basis_vec2, new_basis_vec3]))
mat, col = sympy.Matrix(new_basis).rref()


try:
	matrix = np.linalg.inv(new_basis)
except np.linalg.LinAlgError:
	print('Error. Matrix non-invertible!')

print(np.matmul(matrix, vec_old))