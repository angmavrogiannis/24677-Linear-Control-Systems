import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import sys


def vectorBasisTransformation(new_basis_vec1, new_basis_vec2, new_basis_vec3, vec_old):
  """Transforms the vector in current basis(Cartesian) to new basis.
  
  Steps: 
    Make matrix of the given new basis vectors
    Check linear dependence of matrix using sympy package
    Check matrix invertibility
    If linear dependent and invertible, transform given vector to new basis
  
  Args:
    new_basis_vec1: New basis vector 1
    new_basis_vec2: New basis vector 2
    new_basis_vec3: New basis vector 3
    vec_old: Vector to transform 
    
  Returns:
    matrix: The change of basis matrix from old to new basis.
    vec_new: Vector in new basis.
    
  """  
  
  # **** Insert your code here ****
  
  #Defining the matrix containing the new basis vectors as columns
  new_basis = np.transpose(np.array([new_basis_vec1, new_basis_vec2, new_basis_vec3]))
  
  #Checking linear independence by transforming matrix to reduced row echelon form
  mat, col = Matrix(new_basis).rref()
  lin_indep = False
  matrix = np.empty([new_basis.shape[0],new_basis.shape[1]])
  vec_new = np.empty([len(vec_old)])
  if len(col) == new_basis.shape[1]:
    lin_indep = True
    
  #Checking invertibility, otherwise raising an exception
  invertible = False
  try:
	  matrix = np.linalg.inv(new_basis)
  except np.linalg.LinAlgError:
	  print('Error. Matrix non-invertible!')
  else:
    invertible = True
    
  #Transforming the given vector if the conditions are satisfied
  if lin_indep and invertible:
    vec_new = np.matmul(matrix, vec_old)
  return [matrix, vec_new]
  
if __name__ == "__main__":
  actual_basis_vec1 = np.array([1,0,0])
  actual_basis_vec2 = np.array([0,1, 0])
  actual_basis_vec3 = np.array([0,0,1])
  new_basis_vec1 =  np.array([2,3, 4])
  new_basis_vec2 = np.array([-1,1, 1])
  new_basis_vec3 = np.array([-1,0, 1])
  vec_old = np.array([[2],[-4],[2]])
  
  basis_matrix, vector_new = vectorBasisTransformation(new_basis_vec1, new_basis_vec2, new_basis_vec3,vec_old) 
  
  #Saving the matrices to a dictionary
  solution = {'0':x, '1':y, '2':inner_product, '3':basis_matrix, '4':vector_new}
  np.save("hw2_output.npy", solution)
  
  #plotBasis(actual_basis_vec1, actual_basis_vec2, actual_basis_vec3, new_basis_vec1, new_basis_vec2, new_basis_vec3, vec_new, vec_old)
