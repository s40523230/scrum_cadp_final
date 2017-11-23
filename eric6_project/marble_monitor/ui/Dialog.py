# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog

# for V-rep

from remoteapi import vrep
import sys, math


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.start.clicked.connect(self.start_motor)
        
    def start_motor(self):
        # child threaded script: 
        # 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
        #simExtRemoteApiStart(19999)
         
        vrep.simxFinish(-1)
         
        clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
         
        if clientID!= -1:
            print("Connected to remote server")
        else:
            print('Connection not successful')
            sys.exit('Could not connect')
         
        errorCode,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait)
         
        if errorCode == -1:
            print('Can not find left or right motor')
            sys.exit()
         
        deg = math.pi/180
         
        #errorCode=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint_handle,2, vrep.simx_opmode_oneshot_wait)
         
        def setJointPosition(incAngle, steps):
            for i  in range(steps):
                vrep.simxSetJointPosition(clientID, Revolute_joint_handle, i*incAngle*deg, vrep.simx_opmode_oneshot_wait)
         
        # 每步 10 度, 轉兩圈
        setJointPosition(10, 72)
        # 每步 1 度, 轉兩圈
        #setJointPosition(1, 720)
        # 每步 0.1  度, 轉720 步
        #setJointPosition(0.1, 720)

 
