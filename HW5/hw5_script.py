import numpy as np
from scipy import signal

A = np.array([[-2, 0], [1, 0]])
B = np.array([[1], [0]])
C = np.array([[0, 1]])
D = np.array([[2]])
dt = 0.1
x = np.zeros((2,1))
u = 5

#defining the state space model
sys = signal.StateSpace(A, B, C, D)

#discretizing for T = 0.1s
disc_sys = sys.to_discrete(0.1)

#values for Ad, Bd taken from the output of sys.to_discrete
Ad = disc_sys.A
Bd = disc_sys.B

#loop to calculate x(8)
for i in range(8):
	x = np.matmul(Ad, x) + Bd * u

#calculate y(8) based on the last value of x (= x(8))
y = np.matmul(C, x) + D * u

# Saving all answers
hw5_dict = {}
hw5_dict["x"] = x
hw5_dict["y"] = y
np.save("hw5_output.npy", hw5_dict)