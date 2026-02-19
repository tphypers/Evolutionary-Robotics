import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#setting up simulation world
#gravity
p.setGravity(0,0,c.GRAVITY)
#floor
planeId = p.loadURDF("plane.urdf")
#robot
robotId = p.loadURDF("body.urdf")
#load world
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

#vector to store touch values
backLegSensorValues = numpy.zeros(c.SIM_LENGTH)
frontLegSensorValues = numpy.zeros(c.SIM_LENGTH)
#vector for joint movement
frontTargetAnglesPre = ((numpy.linspace(0, c.TAU, c.SIM_LENGTH)))
backTargetAnglesPre = ((numpy.linspace(0, c.TAU, c.SIM_LENGTH)))
frontTargetAngles = c.FRONT_AMPLITUDE * numpy.sin(c.FRONT_FREQUENCY * frontTargetAnglesPre + c.FRONT_PHASE_OFFSET)
backTargetAngles = c.BACK_AMPLITUDE * numpy.sin(c.BACK_FREQUENCY * backTargetAnglesPre + c.BACK_PHASE_OFFSET)

#running simulation world for a few seconds
for i in range(c.SIM_LENGTH):

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = backTargetAngles[i],
        maxForce = c.BACK_FORCE)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b"Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontTargetAngles[i],
        maxForce = c.FRONT_FORCE)

    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/100)
p.disconnect()
#print(backLegSensorValues)
numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backLegSensorValues.npy", backLegSensorValues)
numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontLegSensorValues.npy", frontLegSensorValues)
