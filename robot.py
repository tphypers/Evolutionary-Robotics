import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as C

class ROBOT:
    def __init__(self, solutionID):
        #robot
        self.myID = solutionID
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.prepare_to_sense()
        self.prepare_to_act()
        #connect to neural network
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system('del brain' + str(solutionID) + '.nndf')

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        with open("./fitness" + str(self.myID) + ".txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * C.motorJointRange
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
                jointName = jointName.decode("utf-8")


    def think(self, step):
        self.nn.Update()
        #self.nn.Print()



