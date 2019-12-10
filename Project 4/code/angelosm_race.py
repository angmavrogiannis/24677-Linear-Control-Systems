from BuggySimulator import *
import numpy as np
import scipy
from util import *
from scipy import signal


class controller():

    def __init__(self,traj, vehicle):
        self.vehicle = vehicle
        self.traj = traj
        self.prev_vx_error = 0
        self.integral_vx_error = 0
        self.curv = self.compute_curvature()
        self.x_k1k1 = np.zeros((4, 1))
        self.p_k1k1 = np.zeros((4, 4))
        self.u = 0

    def compute_curvature(self):
        """Function to compute and return the curvature of trajectory."""
        sigma_gaus = 10
        traj = self.traj
        xp = scipy.ndimage.filters.gaussian_filter1d(input=traj[:,0], sigma=sigma_gaus, order=1)
        xpp = scipy.ndimage.filters.gaussian_filter1d(input=traj[:,0], sigma=sigma_gaus, order=2)
        yp = scipy.ndimage.filters.gaussian_filter1d(input=traj[:,1], sigma=sigma_gaus, order=1)
        ypp = scipy.ndimage.filters.gaussian_filter1d(input=traj[:,1], sigma=sigma_gaus, order=2)
        curv = np.zeros(len(traj))
        for i in range(len(xp)):
            curv[i] = (xp[i] * ypp[i] - yp[i] * xpp[i]) / (xp[i]**2 + yp[i]**2)**1.5

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
        X = vehicle.observation.X
        Y = vehicle.observation.Y 
        xdot = vehicle.observation.xd
        ydot = vehicle.observation.yd 
        phi = vehicle.observation.phi
        phidot = vehicle.observation.phid
        delta = vehicle.observation.delta

        mindist, index = closest_node(X, Y, traj)
        Vx = 8
            
        # Computing the curvature of trajectory
        curv = self.curv

        # ---------------|Lateral Controller|-------------------------
        #Ref Eq (2.45) Vehicle Dynamics and Control by Rajesh Rajamani
        A = np.array([[0,1,0,0],[0,-4*Ca/(m*Vx),4*Ca/m,2*Ca*(lr-lf)/(m*Vx)],[0,0,0,1],[0,2*Ca*(lr-lf)/(Iz*Vx),2*Ca*(lf-lr)/Iz,-2*Ca*(lr*lr+lf*lf)/(Iz*Vx)]])
        B = np.array([[0],[2*Ca/m],[0],[2*Ca*lf/Iz]])
        C = np.identity(4)
        D = np.array([[0],[0],[0],[0]])

        if index < len(traj) - 150:
            idx_fwd = 150
        else:
            idx_fwd = len(traj) - index - 1

        phides = np.arctan2((traj[index + idx_fwd][1] - Y),(traj[index + idx_fwd][0] - X))
        phidesdot = xdot * curv[index + idx_fwd]

        e = np.zeros(4)

        #Ref p34 Vehicle Dynamics and Control by Rajesh Rajamani
        e[0] = (Y - traj[index + idx_fwd][1]) * np.cos(phides) - (X - traj[index + idx_fwd][0]) * np.sin(phides)
        e[2] = wrap2pi(phi - phides)
        e[1] = ydot + xdot * e[2]
        e[3] = phidot - phidesdot

        error = np.matrix(e)

        syscont = signal.StateSpace(A,B,C,D)
        sysdisc = syscont.to_discrete(delT)
        A = sysdisc.A
        B = sysdisc.B
        C = sysdisc.C

        W = np.identity(4) * 0.5
        V = np.identity(4)

        x_kk1 = np.matmul(A, self.x_k1k1) + B * self.u
        
        p_kk1 = np.matmul(np.matmul(A, self.p_k1k1), A.T) + W

        l = np.matmul(np.matmul(p_kk1, C.T),np.linalg.inv(np.matmul(C, np.matmul(p_kk1, C.T)) + V))
        
        x_kk = x_kk1 + np.matmul(l, error.T - np.matmul(C, x_kk1))

        p_kk = np.matmul(np.identity(4) - l @ C, p_kk1)

        Q = np.identity(4)
        R = 1

        S = np.matrix(scipy.linalg.solve_discrete_are(A, B, Q, R))
        K = np.matrix(scipy.linalg.inv(B.T * S * B + R) * (B.T * S * A))

        eigVals, eigVecs = scipy.linalg.eig(A + B * K)
        
        deltades = np.asscalar(np.matmul(-K, x_kk))

        deltad = deltades

        #--------|Longitudinal Controller|------------------------------
        kp = 400
        kd = 300
        ki = -0.1

        # Computing the errors
        vx_error = Vx - xdot
        self.integral_vx_error += vx_error
        derivative_error = vx_error - self.prev_vx_error
        F = kp * vx_error + ki * self.integral_vx_error * delT + kd * derivative_error / delT
        # -----------------------------------------------------------------

        # Communicating the control commands with the BuggySimulator
        controlinp = vehicle.command(F,deltad)
        self.x_k1k1 = x_kk
        self.p_kk1 = p_kk
        self.u = deltad
       
        # Storing the parameters for the next epoch
        self.prev_vx_error = vx_error

        return controlinp
