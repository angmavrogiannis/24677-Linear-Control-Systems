# You dont need to run this script.
# It will be executed by the GradeScope Autograder
# Do not input anything else other than the instructions given in comments, remember that python is tab and caps sensitive.
# In the place of *, input your answer.
# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12. eg: 0.100 -> 0.10

import unittest # Import the gradescope autograder library. No actions are needed here.
import numpy as np # Import numpy lirary. No actions are needed here.
import scipy as spy # No actions are needed here as well.
import math


class AnswersHw6():
	def __init__(self):
		self.exercise_1()
		self.exercise_2()
		self.exercise_3()
		self.exercise_4()
		self.exercise_5()
        
	def exercise_1(self):
		# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer1_P=np.array([[1, 0, 0], [0, 0, -1], [0, -1, 3]])	# controllability matrix 
		self.answer1_controllable = True;	# True: if controllable, False: if not
		self.answer1_Q=np.array([[1, 2, 1], [-1, -2, -1], [1, 2, 1]])	#Observability matrix
		self.answer1_observable = False;	# True: if observable, False: if not
        
	def exercise_2(self):
		# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer2_P=np.array([[0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 2, 1], [0, 0, 2, 1, -1, -1]])	# controllability matrix 
		self.answer2_controllable = True;	# True: if controllable, False: if not
		self.answer2_Q=np.array([[1, 0, 1], [1, 3, -1], [-1, -1, 4]])	#Observability matrix
		self.answer2_observable = True;	# True: if observable, False: if not
        
	def exercise_3(self):
		# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer3_controllable = True;	# True: if controllable, False: if not
		self.answer3_observable = False;	# True: if controllable, False: if not

	def exercise_4(self):
		# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer4_controllable = False;	# True: if controllable, False: if not
		self.answer4_observable = True;		# True: if controllable, False: if not
        
	def exercise_5(self):
		# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer5_eigenvalues = [1];  # Enter the eigen value(s) in the list seperated by commas
        

        
