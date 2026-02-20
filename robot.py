import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        #robot
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.prepare_to_sense()
        self.prepare_to_act()


    def prepare_to_sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    
    def prepare_to_act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)


    def sense(self, step):
         for linkName in self.sensors:
             self.sensors[linkName].Get_Value(step)

    def act(self, step):
         for motorName in self.motors:
             self.motors[motorName].Set_Value(self.robot, step)



