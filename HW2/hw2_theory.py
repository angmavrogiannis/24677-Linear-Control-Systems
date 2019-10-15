# You dont need to run this script.
# It will be executed by the GradeScope Autograder


import unittest # Import the gradescope autograder library. No actions are needed here.
import numpy as np # Import numpy lirary. No actions are needed here.
import scipy as spy # No actions are needed here as well.


class AnswersHw2():
	def __init__(self): # We define a "class". No actions.
		self.exercise_1() # We define a function as a "constructor" No actions needed here, do not remove these statements.
		self.exercise_2() 
		self.exercise_3()
		self.exercise_4()
		self.exercise_5()

	def exercise_1(self):
		"""Real work starts from here.
        Only replace * with your answers. Do not need to change anything else.
		
		Write your answers for question 1 and fill up the variables:

		Question 1: This question has 4 subquestions.
		Determine whether the vectors are linearly dependent or independent

		In the place of *, input your answer.
			0: Linearly dependent
			1: Linearly independent 
		example- 
			self.answer1_1 = 1
			self.answer1_2 = 0

		Do not input anything else, remember that python is tab and caps sensitive.
		The variables here are self.answer1_x_x

	    """
		self.answer1_1 = 1
		self.answer1_2 = 1
		self.answer1_3 = 1
		self.answer1_4 = 0

	def exercise_2(self):
		"""Write your answers for question 2 and fill up the variables:
		
		Question 2: There are 3 subquestions and 2 sub-sub question, one for each vector.
		1) Find the norm 1
		2) Find the norm 2
		3) Find the infinite norm
		whereas 'a' is for vector x1 and 'b' is for x2 in the variable name.

		Write the value obtained till the 2 decimal places, truncated. i.e no flooring 
		or ceiling, directly clip till 2 decimal places.
		In the place of *, input your answer.
		
		example- 
			self.answer2_1_a = 1.01
			self.answer2_1_b = 2.00


		Do not input anything else, remember that python is tab and caps sensitive.
		The variables here are self.answer2_x

		"""
		self.answer2_1_a = 10
		self.answer2_1_b = 3
		self.answer2_2_a = 6.16
		self.answer2_2_b = 1.73
		self.answer2_3_a = 5
		self.answer2_3_b = 1


	def exercise_3(self):
		"""Write your answers for question 3 and fill up the variables:
		
		Question 3: There are 2 sub questions.
		1) Finding the change of basis matrix 
		2) Finding the transformed vector

		Answer will be in form of values. 
		1) The change of basis matrix will be 2x2 and give corresponding values.
		[	x11    x12
			x21    x22	]

		2) The transformed vector is 1x2.
		[	[x11] 
			[x22]	]

		In the place of *, input your answer.
		Must be strictly integers and signed.
		example- 
			self.answer3_1_x11 = 9
			self.answer3_2_x22 = 2


		Do not input anything else, remember that python is tab and caps sensitive.
		The variables here are self.answer3_x

		"""
		self.answer3_1_x11 = 6
		self.answer3_1_x12 = 9
		self.answer3_1_x21 = -2
		self.answer3_1_x22 = -4
		self.answer3_2_x11 = 0
		self.answer3_2_x22 = -2

	def exercise_4(self):
		"""Write your answers for question 4 and fill up the variables:
		
		Question 4: Here, there are 3 subquestions		
		
		First find the basis of the given set of vectors.
		Provide the values of the 2 coefficients in which 
		z, u and v can be expressed in terms of the basis vectors.
		
		Match the values of these alpha and beta
		And rectify if the given vector belongs to the subspace or not.

		In the place of *, input your answer. 
		Provide value in max upto 2 decimal places, truncated. i.e no flooring 
		or ceiling, directly clip till 2 decimal places.
		In the variable name, 1 is for vector z, and 2,3 for u and v
		In case of the answer for subspace
			0: It is in subspace
			1: It is not in the subspace
		This should be strictly be an integer

		example-
			self.answer4_1_alpha = 9.00
			self.answer4_2_subspace = 1
			self.answer4_3_beta = 0.26


		Do not input anything else, remember that python is tab and caps sensitive.
		The variables here are self.answer4_x

		"""
		self.answer4_1_alpha = -1.66
		self.answer4_1_beta = 0.66
		self.answer4_1_subspace = 0
		self.answer4_2_alpha = 0
		self.answer4_2_beta = 0
		self.answer4_2_subspace = 1
		self.answer4_3_alpha = -0.33
		self.answer4_3_beta = -0.66
		self.answer4_3_subspace = 0


	def exercise_5(self):
		"""Write your answers for question 5 and fill up the variables:
		
		Question 5: There are two vectors, find their inner product.
		
		In the place of *, input your answer.
		The value must me in 2 decimal places, truncated. i.e no flooring 
		or ceiling, directly clip till 2 decimal places.

		example- 
			self.answer5 = 25.01

		Do not input anything else, remember that python is tab and caps sensitive.
		The variables here are self.answer5_x

		"""
		self.answer5 = 667




