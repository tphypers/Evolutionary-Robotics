import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as C

class ROBOT:
    def __init__(self, solutionID):
        #block        
        self.block_trajectory = []
        self.block_height = []
        #both
        self.distances = []
        #robot
        self.grabberPositions = []
        self.heights = []
        self.tilts = []
        self.myID = solutionID
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.prepare_to_sense()
        self.prepare_to_act()
        #connect to neural network
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system('del brain' + str(solutionID) + '.nndf')

    def Get_Fitness(self):
        #make block go up.
        avg_block_height = sum(self.block_height) / len(self.block_height)
        #get grabber to block quickly and stay
        avg_distance = sum(self.distances) / len(self.distances)
        #keep torso high to prevent falling over
        avg_height = sum(self.heights) / len(self.heights)
        #keep torso flat to prevent bucking
        avg_tilt = sum(self.tilts) / len(self.tilts)
        fitness = (C.block_distance_weight * -avg_distance) + (C.height_weight * avg_height) - (C.tilt_weight * avg_tilt) + (C.block_height_weight * avg_block_height)
        with open("./fitness" + str(self.myID) + ".txt", "w") as f:
            f.write(str(fitness))

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
        #grabber posittion recording
        stateOfGrabber = p.getLinkState(self.robot,10)
        positionOfGrabber = stateOfGrabber[0]
        self.grabberPositions.append(positionOfGrabber)
        #block position recording
        self.block_pos, block_quat = p.getBasePositionAndOrientation(1) #block bodyID
        self.block_trajectory.append(self.block_pos)
        self.block_height.append(self.block_pos[2] - .5)
        #difference recording
        robot_pos_array = np.array(positionOfGrabber)
        block_pos_array = np.array(self.block_pos)
        self.distances.append(np.linalg.norm(robot_pos_array - block_pos_array))
        #torso position recording
        torso_pos, torso_quat = p.getBasePositionAndOrientation(2) #robot bodyID
        torso_z = torso_pos[2]
        self.heights.append(torso_z)
        toso_pos, torso_quat = p.getBasePositionAndOrientation(2)
        roll, pitch, yaw = p.getEulerFromQuaternion(torso_quat)
        tilt_penalty = abs(roll) + abs(pitch)
        self.tilts.append(tilt_penalty)

        #self.nn.Print()



