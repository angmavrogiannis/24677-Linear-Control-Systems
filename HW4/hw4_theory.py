# You dont need to run this script.
# It will be executed by the GradeScope Autograder
# Do not input anything else other than the instructions given in comments, remember that python is tab and caps sensitive.
# In the place of *, input your answer.

import unittest # Import the gradescope autograder library. No actions are needed here.
import numpy as np # Import numpy lirary. No actions are needed here.
import scipy as spy # No actions are needed here as well.
import math


class AnswersHw4():
	def __init__(self):
		self.exercise_1()
		self.exercise_2()
		# self.exercise_3()
		self.exercise_4()
		self.exercise_5()
		self.exercise_6()

	def exercise_1(self):
		"""Write your answers for question and fill up the variables:
	
		example- 
			self.answer1_1_1 = 3
			self.answer1_1_2 = 2
			self.answer1_1_3 = 1
	    """
	    # Q1 (lambda_1 <= lambda_2 <= lambda_3) where lamda is Eigen value
		self.answer1_1_1 = 1 # lambda_1
		self.answer1_1_2 = 2 # lambda_2
		self.answer1_1_3 = 2 # lambda_3
		# Q2 (lambda_1 <= lambda_2 <= lambda_3)
		self.answer1_2_1 = -2 # lambda_1
		self.answer1_2_2 = 1 # lambda_2
		self.answer1_2_3 = 3 # lambda_3

	def exercise_2(self):
		# Q1 (lambda_1 <= lambda_2 )
		self.answer2_1_1 = 0 # lambda_1
		self.answer2_1_2 = 25 # lambda_2
		# Q2 (lambda_1 <= lambda_2 )
		self.answer2_2_1 = 0 # lambda_1
		self.answer2_2_2 = 25 # lambda_2
		# Q3 (sigma_1 >= sigma_2 )
		self.answer2_3_1 = 5 # sigma_1 
		self.answer2_3_2 = 0 # sigma_2
		# Q4 (sigma_1 >= sigma_2 )
		self.answer2_4_1 = 2.45 # sigma_1. Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer2_4_2 = 1 # sigma_2. 


	def exercise_3(self):
		"""
		As the answer is analytical, we will check it manually.
		"""
		pass

	def exercise_4(self):
		self.answer4_1 = np.array([[1, 0, 0],[0, 2, 0],[0, 0, 3]]) # Write your calculated Jordan form matrix. 
		self.answer4_2 = np.array([[-1, 0, 0],[0, -1+1j*(-1), 0],[0, 0, -1+1j*1]]) # If an eigenvalue is complex, write it in the form of REAL+1j*IMAGE, where 1j is python's complex datatype.
		self.answer4_3 = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 2]])
		self.answer4_4 = np.array([[0, 1, 0],[0, 0, 1],[0, 0, 0]])

	def exercise_5(self):
		self.answer5_A10 = np.array([[1, 1, 9],[0, 0, 1],[0, 0, 1]])
		self.answer5_A103 = np.array([[1, 1, 102],[0, 0, 1],[0, 0, 1]])
		self.answer5_eAt = np.array([[np.e, np.e - 1, 1],[0, 1, np.e - 1],[0, 0, np.e]]) # use numpy contant np.e for exponential as required.

	def exercise_6(self):
		self.answer6 = np.array([[1, 0, 0],[0, 2, 0],[0, 0, 2]]) # Write your diagonalized matrix.


