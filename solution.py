import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
    
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f'python3 simulate.py {directOrGUI}')
        with open("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\fitness.txt") as fitnessFile:
            self.fitness = float(fitnessFile.read())
    
    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row][column] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name=f"Box", pos=[-2,-2,.5] , size=[1,1,1])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name=f"Torso", pos=[0,0,1.5] , size=[1,1,1])
        pyrosim.Send_Cube(name=f"BackLeg", pos=[-.5,0,-.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
        pyrosim.Send_Cube(name=f"FrontLeg", pos=[.5,0,-.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
        pyrosim.End()

    def Create_Brain(self):
        #intialize neural network
        pyrosim.Start_NeuralNetwork("brain.nndf")

        #sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        #motor neurons
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

        #synapses
        for currentRow in range(0,3):
            for currentColumn in  range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
