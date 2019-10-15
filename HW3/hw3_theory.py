# You dont need to run this script.
# It will be executed by the GradeScope Autograder
# Do not input anything else other than the instructions given in comments, remember that python is tab and caps sensitive.
# In the place of *, input your answer.

import unittest # Import the gradescope autograder library. No actions are needed here.
import numpy as np # Import numpy lirary. No actions are needed here.
import scipy as spy # No actions are needed here as well.


class AnswersHw3(): # We define a "class". No actions.

	def __init__(self): # We define a function as a "constructor"
		self.exercise_1()
		self.exercise_2()
		self.exercise_3()
		self.exercise_4()
		self.exercise_5()
		self.exercise_6()
		self.exercise_7()

	def exercise_1(self):
		"""Real work starts from here.

		Find the solution i.e the vectors v1, v2, v3.
		Input your answer vector as a numpy array.
		Make sure the values of the elements in the vector is correct within 3 decimal places.

		example- 
			self.v1 = np.array([1.0, 2.0, 3.0])

		"""
		self.v1 = np.array([0.447, 0.894, 0.000])
		self.v2 = np.array([0.333, -0.752, -0.568])
		self.v3 = np.array([0.364, -0.821, -0.438])


	def exercise_2(self):
		"""
		Input your answer vector as a numpy array
		example- 
			self.answer2 = np.array([1.0, 2.0, 3.0])
		"""
		self.answer2 = np.array([-5/3, 1/3, 1])


	def exercise_3(self):
		"""
		example- 
			self.answer3_1 = 1
			self.answer3_2 = np.array([1, 2, 3])
		"""
		self.answer3_1 = 0.696 # Minimum distance
		self.answer3_2 = np.array([-32/132, -80/132, 32/132]) # Projection point

	def exercise_4(self):
		"""
		1) Whether solution  exists - 
			0: yes
			1: No 

		2) Is solution unique - 
			0: yes
			1: No 

		3) Does solution exist - 
			0: yes
			1: No 

		example- 
			self.answer4_1 = 1
			self.answer4_2 = 0
			self.answer4_3 = 1

		"""
		self.answer4_1 = 0
		self.answer4_2 = 0
		self.answer4_3 = 1


	def exercise_5(self):
		"""
		1) Finding the general solution:
			Substitute value x_{3} = 1 and provide the answer for the following:
		example-
			self.answer5_x1 = 1
			self.answer5_x2 = 0
			self.answer5_x3 = 2
			self.answer5_x4 = 5

		2) Finding the solution with smallest euclidean distance.
			Find the variable that piviots the complete solution, provide 
			the value of that variable for which the distance is smallest.
		example-
			self.answer5_x = 1

		"""
		self.answer5_x1 = 0
		self.answer5_x2 = -2
		self.answer5_x3 = 1
		self.answer5_x4 = 1
		self.answer5_x = 1/6

	def exercise_6(self):
		"""
		example-
			self.answer6_1_rank = 3
			self.answer6_1_nullity = 1
	
		"""
		self.answer6_1_rank = 2
		self.answer6_1_nullity = 1
		self.answer6_2_rank = 3
		self.answer6_2_nullity = 0
		self.answer6_3_rank = 3
		self.answer6_3_nullity = 1


	def exercise_7(self):
		"""
		Answer as follows:
			0: Linear
			1: Non-linear

		example-
			self.answer7_1 = 1
	
		"""
		self.answer7_1 = 1
		self.answer7_2 = 0
		self.answer7_3 = 0
		self.answer7_4 = 0


