
from BuggySimulator import *
import numpy as np
import scipy
import cmath
from scipy.ndimage import gaussian_filter1d
from util import *
from scipy import signal
import control
    
class controller():
    
    def __init__(self,traj,vehicle):
        self.vehicle = vehicle
        self.traj = traj
        self.prev_vx_error = 0
        self.integral_vx_error = 0
        self.curv = self.compute_curvature()
    
    def compute_curvature(self):
        Xdot = gaussian_filter1d(self.traj[:, 0], sigma=10, order=1)
        Xddot = gaussian_filter1d(self.traj[:,0], sigma=10, order=2)
        Ydot = gaussian_filter1d(self.traj[:,1], sigma=10, order=1)
        Yddot = gaussian_filter1d(self.traj[:,1], sigma=10, order=2)
        curv = np.divide((np.multiply(Xdot, Yddot) - np.multiply(Ydot, Xddot)), np.power((np.square(Xdot)) + np.square(Ydot), 1.5))
        return curv

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


        delT = 0.05

        #reading current vehicle states
        X = vehicle.state.X
        Y = vehicle.state.Y
        xdot = vehicle.state.xd
        ydot = vehicle.state.yd
        phi = vehicle.state.phi
        phidot = vehicle.state.phid
        delta = vehicle.state.delta

        #Set time horizon (look ahead)
        time_horizon = 50
        _, closest_index = closest_node(X,Y,traj)

        if time_horizon + closest_index >= 8203:
            time_horizon = 0

        #Get desired values
        Vx = 4.3
        X_desired = traj[closest_index + time_horizon,0]
        Y_desired = traj[closest_index + time_horizon,1]
        phi_desired = np.arctan2(Y_desired - Y, X_desired - X)

        # ---------------|Lateral Controller|-------------------------
        A = np.array([[0, 1, 0, 0], [0, -4*Ca / (m * xdot), 4*Ca/m, (2*Ca*(lr - lf))/(m*xdot)], [0, 0, 0, 1], [0, (2*Ca*(lr - lf)) / (Iz * xdot), (2*Ca*(lf - lr)) / Iz, (-2*Ca*(np.power(lf, 2) + np.power(lr, 2))) / (Iz * xdot)]])
        B = np.array([[0], [2*Ca / m], [0], [(2 * Ca* lf) / Iz]])

        P = np.array([-100, -10, -5, 0])

        K = control.place(A, B, P)

        #e1 = -(Y - Y_desired) * np.sin(phi_desired) + (Y - Y_desired) * np.cos(phi_desired)
        e1 = 0
        e2 = wrap2pi(phi - phi_desired)
        e1dot = ydot + xdot * e2
        #e2dot = phidot - xdot / self.curv[closest_index + time_horizon]
        e2dot = phidot

        e = np.hstack((e1, e1dot, e2, e2dot))

        deltad = (-np.asscalar(np.matmul(K, e)) - delta) / delT

        #--------|Longitudinal Controller|------------------------------
        kp = 400
        kd = 300
        ki = -0.1

        vx_error = Vx - xdot
        self.integral_vx_error += vx_error
        derivative_error = vx_error - self.prev_vx_error
        F = kp * vx_error + ki * self.integral_vx_error * delT + kd * derivative_error / delT

        # -----------------------------------------------------------------

        # Communicating the control commands with the BuggySimulator
        controlinp = vehicle.command(F,deltad)
        # F: Force
        # deltad: desired rate of steering command
        self.prev_vx_error = vx_error

        return controlinp