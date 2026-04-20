import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as C

class SOLUTION:
    def __init__(self, ID):
        self.weights = np.random.rand(C.numSensorNeurons, C.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = ID
        
    def Wait_For_Simulation_To_End(self):
        fitnessFile = f"fitness{self.myID}.txt"
        bodyFile = "body" + str(self.myID) + ".urdf"
        worldFile = "world"  + str(self.myID) + ".sdf"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01) 
        while os.stat(fitnessFile).st_size == 0:
            time.sleep(0.01)
        with open(fitnessFile, "r") as f:
            content = f.read()
            if content == "":
                time.sleep(0.1)
                return self.Wait_For_Simulation_To_End()
            self.fitness = float(content)
        os.system(f"del {fitnessFile}")
        os.system(f"del {bodyFile}")
        os.system(f"del {worldFile}")

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system('start /B python simulate.py ' + directOrGUI + ' '+ str(self.myID))
            
    def SetID(self, ID):
        self.myID = ID

    def Mutate(self):
        row = random.randint(0,C.numSensorNeurons-1)
        column = random.randint(0,C.numMotorNeurons-1)
        self.weights[row][column] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world"  + str(self.myID) + ".sdf")
        pyrosim.Send_Cube(name=f"Box", pos=[5,0,.375] , size=[.75,.75,.75])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        pyrosim.Send_Cube(name=f"Torso", pos=[0,0,1] , size=[2,1,.5])

        ### back right
        pyrosim.Send_Cube(name=f"BackLeg", pos=[-.5,0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-1,-.5,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name=f"BackLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        
        ### back left
        pyrosim.Send_Cube(name=f"LeftLeg", pos=[-.5,0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-1,.5,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name=f"LeftLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        
        ### front left
        pyrosim.Send_Cube(name=f"FrontLeg", pos=[-.5,0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,.5,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name=f"FrontLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        
        ### front right
        pyrosim.Send_Cube(name=f"RightLeg", pos=[-.5,0,0] , size=[1,.2,.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [1,-.5,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name=f"RightLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        
        ### neck base
        pyrosim.Send_Cube(name=f"NeckBase", pos=[0,0,.5], size=[.1,.1,1])
        pyrosim.Send_Joint( name = "Torso_NeckBase" , parent= "Torso" , child = "NeckBase" , type = "revolute", position = [.75, 0, 1], jointAxis = "0 1 1")

        ### neck arm
        pyrosim.Send_Cube(name=f"NeckArm", pos=[.5,0,0], size=[1,.1,.1])
        pyrosim.Send_Joint( name = "NeckBase_NeckArm", parent= "NeckBase" , child = "NeckArm" , type = "revolute", position = [0, 0, 1], jointAxis = "1 1 0")

        ### GRABBER
        #center
        pyrosim.Send_Cube(name=f"GrabberCenter", pos=[0,0,0], size=[.1,1,.1])
        pyrosim.Send_Joint( name = "NeckArm_GrabberCenter", parent= "NeckArm", child = "GrabberCenter", type = "revolute", position = [1, 0, 0], jointAxis ="0 1 0")
        #left
        pyrosim.Send_Cube(name=f"GrabberRight", pos=[.5,0,0], size=[1,.1,.1])
        pyrosim.Send_Joint( name = "GrabberCenter_GrabberRight", parent= "GrabberCenter", child = "GrabberRight", type = "revolute", position = [0, -.5, 0], jointAxis ="0 0 1")
        #right
        pyrosim.Send_Cube(name=f"GrabberLeft", pos=[.5,0,0], size=[1,.1,.1])
        pyrosim.Send_Joint( name = "GrabberCenter_GrabberLeft", parent= "GrabberCenter", child = "GrabberLeft", type = "revolute", position = [0, .5, 0], jointAxis ="0 0 1")
        
        pyrosim.End()

    def Create_Brain(self):
        #intialize neural network
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        #sensor neurons
        #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        #pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg") ### front left
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg") ### back right
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg") ### back left
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg") ### front right
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "GrabberRight") ### right grabber
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "GrabberLeft") ### left grabber


        #motor neurons
        pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_BackLeg") ### back right
        pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_FrontLeg") ### front left
        pyrosim.Send_Motor_Neuron(name = 8 , jointName = "Torso_LeftLeg") ### back left
        pyrosim.Send_Motor_Neuron(name = 9 , jointName = "Torso_RightLeg") ### front right
        pyrosim.Send_Motor_Neuron(name = 10 , jointName = "FrontLeg_FrontLowerLeg") ### front left
        pyrosim.Send_Motor_Neuron(name = 11 , jointName = "BackLeg_BackLowerLeg") ### back right
        pyrosim.Send_Motor_Neuron(name = 12 , jointName = "LeftLeg_LeftLowerLeg") ### back left
        pyrosim.Send_Motor_Neuron(name = 13 , jointName = "RightLeg_RightLowerLeg") ### front right
        pyrosim.Send_Motor_Neuron(name = 14 , jointName = "Torso_NeckBase") ### neck base
        pyrosim.Send_Motor_Neuron(name = 15 , jointName = "NeckBase_NeckArm") ### neck arm
        pyrosim.Send_Motor_Neuron(name = 16 , jointName = "NeckArm_GrabberCenter") ### grabber center
        pyrosim.Send_Motor_Neuron(name = 17 , jointName = "GrabberCenter_GrabberRight") ### grabber right
        pyrosim.Send_Motor_Neuron(name = 18 , jointName = "GrabberCenter_GrabberLeft") ### grabber left

        #synapses
        for currentRow in range(0, C.numSensorNeurons):
            for currentColumn in range(0, C.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + C.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
