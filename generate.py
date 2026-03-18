import pyrosim.pyrosim as pyrosim
import random

#world creation
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name=f"Box", pos=[-2,-2,.5] , size=[1,1,1])
    pyrosim.End()

#Robot creation
def Create_Robot():
    pass

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name=f"Torso", pos=[0,0,1.5] , size=[1,1,1])
    pyrosim.Send_Cube(name=f"BackLeg", pos=[-.5,0,-.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name=f"FrontLeg", pos=[.5,0,-.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,0,1])
    
    
    pyrosim.End()

def Generate_Brain():
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
    for sensor_neuron in range(0,3):
        for motor_neuron in  range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName = sensor_neuron, targetNeuronName = motor_neuron, weight = random.uniform(1,-1))
            

    #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -.5 )
    #pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1 )
    #pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = .5 )
    #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = .5 )

    pyrosim.End()

Generate_Body()
Generate_Brain()
Create_Robot()
Create_World()

