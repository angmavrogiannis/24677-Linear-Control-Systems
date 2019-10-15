# Importing required packages. Limited to only numpy.
import numpy as np
from numpy.linalg import matrix_rank

np.random.seed(0) # Seed for randomized items, ignore this line.

# We define class named Homework3
class Homework3():
  
  #class constructor
  def __init__(self):
    # x, y and z array of point coordinates for Qs3. e.g: self.x
    # ___ write your code here _____
    self.x_inner = np.empty
    self.y_inner = np.empty
    self.inner_product = 0
    self.v1 = np.empty
    self.v2 = np.empty
    self.v3 = np.empty
    self.x = np.empty
    self.y = np.empty
    self.z = np.empty
    self.projection_points = np.empty

  def Compute_inner_products(self):
    """   
    Function to compute inner products 
    
    Saves:
      inner_product: inner-products of given vectors

    """
    # ___ write your code here _____
    #ip = np.inner(self.inner_x, self.inner_y)
    self.inner_product = np.inner(self.x_inner, self.y_inner) 

  
  def Compute_dimention(self):
    """
    Function to compute dimention
    
    Saves:
      dimention: dimention of given vectors

    """
    # ___ write your code here _____
    mat = np.array([self.v1, self.v2, self.v3])
    self.dimention = matrix_rank(mat)

      
      
  def Project_points(self, a, b, c):
    """
    Function to project the points with coordinates x, y, z onto the plane defined by a*x + b*y + c*z = 1
    
    Args:
      a: Plane coefficent
      b: Plane coefficent
      c: Plane coefficent
      
    Saves:
      projection_points: projection vectors of the projected point

    """
    # ___ write your code here _____
    self.projection_points = np.empty([10,3])
    for i in range(10):
      t = (- a * self.x[i] - b * self.y[i] - c * self.z[i]) / (a * a + b * b + c * c)
      self.projection_points[i][0] = a * t + self.x[i]
      self.projection_points[i][1] = b * t + self.y[i]
      self.projection_points[i][2] = c * t + self.z[i]


# main function
def main():
  
  answer = Homework3()  # Construct an object of the Homework3 class
  
  # Question 1
  x_inner = np.arange(24).reshape((2,3,4)) # matrix construction same as in homwork 2
  y_inner = np.arange(4)
  answer.x_inner = x_inner # Use the provided variable names (x_inner) in the class. Define the variable in class constructor to initialize. 
  answer.y_inner = y_inner # Initialization for the variable belonging to Homework3 object.  
  
  # Question 2
  v1 = np.asarray([1,2,2,1])
  v2 = np.asarray([1,1,0,1])
  v3 = np.asarray([3,5,4,3])
  answer.v1 = v1 # Use the given variable (v1, v2 ... etc)
  answer.v2 = v2
  answer.v3 = v3
 
  # Question 3
  x = np.random.rand(10) # Generating random 10 point coordinates (x,y,z)
  y = np.random.rand(10)
  z = np.random.rand(10)
  a = 10
  b = 15
  c = 1
  d = 7
  answer.x = x # x, y, z values are initailized
  answer.y = y
  answer.z = z

  answer.Compute_inner_products() # We call the class function to compute inner products from the initialized values.
  answer.Compute_dimention()
  answer.Project_points(a, b, c) # a, b, c are inputs to the function. 
  
  # Saving all answers
  hw3_dict = {}
  hw3_dict["0"] = x_inner
  hw3_dict["1"] = y_inner
  hw3_dict["2"] = answer.inner_product # The computed inner product is saved in variable "inner_product" of Homework3 object, save it into a dictionary
  hw3_dict["3"] = answer.dimention # The computed dimention is saved in variable "inner_product" of Homework3 object, save it into a dictionary
  hw3_dict["4"] = np.array([x,y,z])
  hw3_dict["5"] = answer.projection_points # The computed projection_points is saved in variable "inner_product" of Homework3 object, save it into a dictionary
 
  print("The inner product is: {}".format(hw3_dict["2"]))
  print("The dimention is: {}".format(hw3_dict["3"]))
  print("The given point coordinates are :\n {}, {}, {}".format(x , y, z))
  print("The projected points are: \n {}".format(hw3_dict["5"]))
  np.save("hw3_output.npy", hw3_dict)

if __name__ == "__main__":
  main()