# You dont need to run this script.
# It will be executed by the GradeScope Autograder
# Do not input anything else other than the instructions given in comments, remember that python is tab and caps sensitive.
# In the place of *, input your answer.
# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12. eg: 0.100 -> 0.10

import unittest # Import the gradescope autograder library. No actions are needed here.
import numpy as np # Import numpy lirary. No actions are needed here.
import scipy as spy # No actions are needed here as well.
import math


class AnswersHw7():

	def __init__(self):
		self.exercise_1()
		self.exercise_2()
		self.exercise_3()
		self.exercise_4()

	def exercise_1(self):
		self.answer1_a_Lyapunov_stable = True;  # True: if stable, False: if not
		self.answer1_a_saymptotically_stable = False;  # True: if stable, False: if not
		self.answer1_a_eigenvalues = [0.5, 1]; # Enter the eigen value(s) in the list seperated by commas
                                          # Please round to 2 decimals, order doesn't matter
		self.answer1_b_Lyapunov_stable = True;  # True: if stable, False: if not
		self.answer1_b_saymptotically_stable = True;  # True: if stable, False: if not
		self.answer1_b_eigenvalues = [-5, -3, -1]; # Enter the eigen value(s) in the list seperated by commas
                                          # Please round to 2 decimals, order doesn't matter
        
	def exercise_2(self):
		# Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer2_1_L2norm = 3.62;
		self.answer2_2_NuclearNorm = 13.15;
		self.answer2_2_HSNorm = 10.63;
		self.answer4_3_L1norm = 6.00;
		self.answer4_3_L2norm = 5.46;
		self.answer4_3_Linfnorm = 7.00;

	def exercise_3(self):       
        # Round your answers to 2 decimals. eg: 0.114 -> 0.11, 0.115 -> 0.12 
		self.answer3_cost = 132.50;

	def exercise_4(self):
        	self.answer4 = np.array([[np.exp(4), 0, 0, 0, 0, 0], [0, np.exp(2), 2 * np.exp(2), 2 * np.exp(2), 0, 0], [0, 0, np.exp(2), 2 * np.exp(2), 0, 0], [0, 0, 0, np.exp(2), 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, np.exp(-2)]]);

