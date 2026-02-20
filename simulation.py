from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time

class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)
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
            self.robot.act(step)
            time.sleep(1/60)
            '''
           '''

#destructors
    def __del__(self):
        p.disconnect()



