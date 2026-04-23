import numpy
import math
import random

#constants

#bot body construction
body_type = "A" #"B" for flipped legs

#gravity
GRAVITY = -9.8
#length of each simulation
SIM_LENGTH = 1000
#number of generations
GENERATIONS = 50
#population size
POPULATION_SIZE = 50

#Fitness weights
block_height_weight = 1.2
tilt_weight = 1
height_weight = .5
block_distance_weight = 1

#------Motor control------
#range of motion
TAU = 2 * math.pi
motorJointRange = .75
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
numSensorNeurons = 6
numMotorNeurons = 13
