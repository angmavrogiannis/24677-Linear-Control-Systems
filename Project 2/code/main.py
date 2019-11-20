from BuggySimulator import *
import numpy as np
from controller import *
from util import *
import matplotlib.pyplot as plt
from Evaluation import *


# get the trajectory
traj = get_trajectory('buggyTrace.csv')


# initialise the Buggy
vehicle = initail(traj, 0)
print(vehicle.state.showState())

n = 25000
X = []
Y = []
delta = []
xd = []
yd = []
phi = []
phid = []
deltad = []
F = []
minDist =[]


# preprocess the trajectory
passMiddlePoint = False
nearGoal = False

# Instantiate an object for the controller class
controlV=controller(traj,vehicle)

for i in range(n):
    command = controlV.control_update()
    vehicle.update(command = command)

    # termination check
    disError,nearIdx = closest_node(vehicle.state.X, vehicle.state.Y, traj)
    stepToMiddle = nearIdx - len(traj)/2.0
    if abs(stepToMiddle) < 100.0 and passMiddlePoint==False:
        passMiddlePoint = True
        print('middle point passed')
    nearGoal = nearIdx >= len(traj)-50
    if nearGoal and passMiddlePoint:
        print('...... destination reached!.............')
        break
    

    # record states
    X.append(vehicle.state.X)
    Y.append(vehicle.state.Y)
    delta.append(vehicle.state.delta)
    xd.append(vehicle.state.xd)
    yd.append(vehicle.state.yd)
    phid.append(vehicle.state.phid)
    phi.append(vehicle.state.phi)
    deltad.append(command.deltad)
    F.append(command.F)
    minDist.append(disError)

np.savez('BuggyStates.npz',X=X,Y=Y,delta=delta,xd=xd,yd=yd,phid=phid,
phi=phi,deltad=deltad,F=F,minDist=minDist)

StateSave = np.transpose(np.array([xd,yd,phid,delta,X,Y,phi]))
np.save('24-677_Project_BuggyStates.npy',StateSave)

showResult(traj,X,Y,delta,xd,yd,F,phi,phid,minDist)
evaluation(minDist, traj, X, Y)
