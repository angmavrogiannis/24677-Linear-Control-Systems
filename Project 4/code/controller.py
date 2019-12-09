
from BuggySimulator import *
import numpy as np
import scipy
from util import *


class controller():

    def __init__(self,traj, vehicle):

        self.vehicle=vehicle
        self.traj=traj
        self.curv=self.compute_curvature()

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


        # ---------------|Lateral Controller|-------------------------
        """
        Design your lateral controller here. 
        .

        .
        .
        .
        .
        .
        """

        #--------|Longitudinal Controller|------------------------------
        """
        Desing your longitudinal controller here
        .
        .
        .
        .
        .
        .
        .

        """
        # -----------------------------------------------------------------

        # Communicating the control commands with the BuggySimulator
        controlinp = vehicle.command(F,deltad)
        # F: Force
        # deltad: desired rate of steering command
       

        return controlinp
