# You dont need to run this script.
# It will be executed by the GradeScope Autograder


import unittest # Import the gradescope autograder library. No actions are needed here.
import numpy as np # Import numpy lirary. No actions are needed here.
import scipy as spy # No actions are needed here as well.


class AnswersHw1(): # We define a "class". No actions.
    def __init__(self): # We define a function as a "constructor"
        self.exercise_1() # No actions needed here, do not remove these statements.
        self.exercise_2()
        self.exercise_3()
        self.exercise_4()
        self.exercise_5()
        self.exercise_6()

    def exercise_1(self):
        """Real work starts from here.
        Only replace * with your answers. Do not need to change anything else.
        Remember that python is tab and caps sensitive.
        """
        self.answer1_1_a = 1 # Replace * with 0 if the system is non-linear, 1 if linear
        self.answer1_1_b = 0 # 0: time-invariant, 1: time-varying
        self.answer1_2_a = 0 # Same as above
        self.answer1_2_b = 0
        self.answer1_3_a = 1
        self.answer1_3_b = 1
        self.answer1_4_a = 1
        self.answer1_4_b = 1
        self.answer1_5_a = 1
        self.answer1_5_b = 0
        self.answer1_6_a = 1
        self.answer1_6_b = 0
        self.answer1_7_a = 0
        self.answer1_7_b = 0
        self.answer1_8_a = 1
        self.answer1_8_b = 1


    def exercise_2(self):
        self.answer2_1 = 0     # 0: It is not a field, 1: It is a field
        self.answer2_2 = 1
        self.answer2_3 = 0
        self.answer2_4 = 1


    def exercise_3(self):
        self.answer3_1 = 1     # 0: It is not a subspace, 1: It is a subspace
        self.answer3_2 = 1
        self.answer3_3 = 1
        self.answer3_4 = 0


    def exercise_4(self):
        self.answer4 = np.array([[0 , 1], [2 , -1]])
        # This is how you define a matrix in python.
        # Replace *s with the four items in the matrix.
        # codeacademy link : https://www.codecademy.com/learn/intro-statistics-numpy/modules/dspath-intro-numpy


    def exercise_5(self):
        self.inputs = 4
        self.states = 3
        self.outputs = 2

    def exercise_6(self):
        # Substitute m = 1, l = 1, g = 10, M  = 1, I = 1 and write down your answer. 
        # For floating numbers truncate your number to 2 decimals manually and type in your answer. You can use python methods otherwise.
        self.answer6_A = np.array([[0 , 1, 0, 0], [0 , 0, -3.33, 0],  [0 , 0, 0, 1],  [0 , 0, 6.66, 0]])
        self.answer6_B = np.array([0 , 0.66, 0, -0.33])
