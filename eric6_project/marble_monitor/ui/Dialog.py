# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog

# for V-rep
from remoteapi import vrep
import sys
import threading
import time


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
        self.count = 0
        self.clientID = 0
        self.very_beginning = True
        self.make = threading.Thread(target=self.start_thread)
        self.pill2kill = threading.Event()
        self.display.setText(str(self.count))
        self.start.clicked.connect(self.start_motor)
        self.stop.clicked.connect(self.stop_motor)
        self.pause.clicked.connect(self.pause_motor)
        
    def start_motor(self):
        # 利用執行緒執行 start
        if self.very_beginning:
            self.make.start()
            self.very_beginning = False
        else:
            self.pill2kill.set
            #啟動模擬
            vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot)
     
    def stop_motor(self):
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
        
    def pause_motor(self):
        # 暫停執行緒, 暫停模擬
        #time.sleep(2)
        self.pill2kill.clear()
        # 暫停模擬
        vrep.simxPauseSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)
        
    def start_thread(self):
        # child threaded script: 
        # 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
        #simExtRemoteApiStart(19999)
         
        vrep.simxFinish(-1)
         
        self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
        
        #啟動模擬
        vrep.simxStartSimulation(self.clientID, vrep.simx_opmode_oneshot)
        
        if self.clientID!= -1:
            print("Connected to remote server")
        else:
            print('Connection not successful')
            sys.exit('Could not connect')
         
        errorCode1, Revolute_joint_handle = vrep.simxGetObjectHandle(self.clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait)
        errorCode2, sensorHandle = vrep.simxGetObjectHandle(self.clientID,'Finish',vrep.simx_opmode_oneshot_wait)
        
        if errorCode1 == -1:
            print('Can not find left or right motor')
            sys.exit()
            
        while vrep.simxGetConnectionId(self.clientID) != -1:
            (errorCode3, detectionState1, detectedPoint1, detectedObjectHandle1, detectedSurfaceNormalVector1) = vrep.simxReadProximitySensor(self.clientID, sensorHandle, vrep.simx_opmode_streaming)
            if errorCode3 == vrep.simx_return_ok:
                if detectionState1:
                    self.count += 1
                    print("通過球總數:", self.count)
                    
            self.display.setText(str(self.count))
            vrep.simxSetJointTargetVelocity(self.clientID, Revolute_joint_handle, 0.5, vrep.simx_opmode_oneshot_wait)
    
        #終止模擬
        vrep.simxStopSimulation(self.clientID, vrep.simx_opmode_oneshot_wait)

 
