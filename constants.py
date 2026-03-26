import numpy
import math
import random

#constants

#gravity
GRAVITY = -9.8
#length of each simulation
SIM_LENGTH = 1000
#number of generations
GENERATIONS = 10
#population size
POPULATION_SIZE = 10



#------Motor control------
#range of motion
TAU = 2 * math.pi
motorJointRange = .5
#amplitude 
FRONT_AMPLITUDE = math.pi/4
BACK_AMPLITUDE = math.pi/4
#frequency
FRONT_FREQUENCY = 10
BACK_FREQUENCY = 10
#phase offset
FRONT_PHASE_OFFSET = 0
BACK_PHASE_OFFSET = .75
#maximum force
FRONT_FORCE = 100
BACK_FORCE = 100

#---BRAIN----
numSensorNeurons = 4
numMotorNeurons = 8
