from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time

class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "GUI":
            physicsClient = p.connect(p.GUI)
        else:
            physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        #setting up simulation world
        p.setGravity(0,0,c.GRAVITY)
        self.Run()

# runs simulation for length specified in SIM_LENGTH
    def Run(self):
        for step in range(c.SIM_LENGTH):
            p.stepSimulation()
            self.robot.sense(step)
            self.robot.think(step)
            self.robot.act(step)
            if self.directOrGUI == "GUI":
                time.sleep(1/200)
            
    def Get_Fitness(self):
        self.robot.Get_Fitness()
           

#destructors
    def __del__(self):
        p.disconnect()



