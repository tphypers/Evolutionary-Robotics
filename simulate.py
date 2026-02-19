import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#setting up simulation world
#gravity
p.setGravity(0,0,-9.8)
#floor
planeId = p.loadURDF("plane.urdf")
#robot
robotId = p.loadURDF("body.urdf")
#load world
p.loadSDF("world.sdf")

iterations = 1000
pyrosim.Prepare_To_Simulate(robotId)
#vector to store touch values
backLegSensorValues = numpy.zeros(iterations)
frontLegSensorValues = numpy.zeros(iterations)
#vector for joint movement
frontTargetAnglesPre = ((numpy.linspace(0, 2 * numpy.pi, iterations)))
backTargetAnglesPre = ((numpy.linspace(0, 2 * numpy.pi, iterations)))

#front
famplitude = math.pi/4
ffrequency = 10
fphaseOffset = 0
#back
bamplitude = math.pi/4
bfrequency = 10
bphaseOffset = .75

frontTargetAngles = famplitude * numpy.sin(ffrequency * frontTargetAnglesPre + fphaseOffset)
#numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontTargetAngles.npy", frontTargetAngles)
backTargetAngles = bamplitude * numpy.sin(bfrequency * backTargetAnglesPre + bphaseOffset)
#numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backTargetAngles.npy", backTargetAngles)
#exit()
#running simulation world for a few seconds
for i in range(iterations):

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = backTargetAngles[i],
        maxForce = 30)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b"Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontTargetAngles[i],
        maxForce = 30)

    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/100)
p.disconnect()
#print(backLegSensorValues)
numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backLegSensorValues.npy", backLegSensorValues)
numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontLegSensorValues.npy", frontLegSensorValues)
