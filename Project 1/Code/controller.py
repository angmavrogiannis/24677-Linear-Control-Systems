from BuggySimulator import *
import numpy as np
import scipy
from scipy.ndimage import gaussian_filter1d
from util import *
import scipy.signal
    
class controller():
    
    def __init__(self,traj,vehicle):
        self.vehicle = vehicle
        self.traj = traj

        # Add additional member variables according to your need here.
        self.cumulative_error = 0
        self.previous_error = 0
        
    def calc_PID_input(self, current_error, kp, ki, kd):
        delT = 0.05
        self.cumulative_error += current_error * delT
        error_differrential = (current_error - self.previous_error) / delT
        self.previous_error = current_error
        pid_input = kp * current_error + ki * self.cumulative_error + kd * error_differrential
        return pid_input


    def control_update(self):

        traj=self.traj
        vehicle=self.vehicle 
        
        lr = vehicle.lr
        lf = vehicle.lf
        Ca = vehicle.Ca
        Iz = vehicle.Iz
        f = vehicle.f
        m = vehicle.m
        g = vehicle.g

        delT = 0.05   # The simulator runs at a constant fps.

        #reading current vehicle states
        X = vehicle.state.X
        Y = vehicle.state.Y
        xdot = vehicle.state.xd
        ydot = vehicle.state.yd
        phi = vehicle.state.phi
        phidot = vehicle.state.phid
        delta = vehicle.state.delta

        #Vx = 6

        #Set predetermined future time horizon and get closest corresponding trajectory node
        time_horizon = 20
        _, closest_index = closest_node(X,Y,traj)

        if time_horizon + closest_index >= 8203:
            time_horizon = 0

        #Get desired values
        X_desired = traj[closest_index + time_horizon,0]
        Y_desired = traj[closest_index + time_horizon,1]
        phi_desired = np.arctan2(Y_desired - Y, X_desired - X)

        # ---------------|Lateral Controller|-------------------------        
        phi_error = wrap2pi(phi_desired - phi)
        
        deltad = self.calc_PID_input(phi_error, 15, 0., 0.)      

        #--------|Longitudinal Controller|------------------------------
        position_error = np.power(np.power(X_desired - X, 2) + np.power(Y_desired - Y, 2), 0.5)
        velocity_error = position_error / delT
        
        F = self.calc_PID_input(velocity_error, 5, 0.000001, 0.00001)
        
        # Communicating the control commands with the BuggySimulator
        controlinp = vehicle.command(F,deltad)
        # F: Force
        # deltad: desired rate of steering command
        Vx = xdot
        return controlinp,Vx