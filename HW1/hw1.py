import numpy as np
import scipy as spy

# **** Insert your code here ****

#Creating a random 3x3 matrix A
A = np.random.rand(3,3)

#Finding the inverse of the above matrix
invA = np.linalg.inv(A)

#Finding the determinant of matrix A
detA = np.linalg.det(A)

#Normalizing matrix A
Amax = np.amax(A)
Amin = np.amin(A)
Anorm = np.zeros((3,3))
for i in range(3):
  for j in range(3):
    Anorm[i,j] = (A[i,j] - Amin) / (Amax - Amin)
    
#Saving the matrices to a dictionary
Adict = {'0':A, '1':invA, '2':detA, '3':Anorm}
np.save("hw1_output.npy", Adict)
