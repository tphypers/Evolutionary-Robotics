import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

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


pyrosim.Prepare_To_Simulate(robotId)
#vector to store touch values
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
#running simulation world for a few seconds
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)
p.disconnect()
#print(backLegSensorValues)
numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backLegSensorValues.npy", backLegSensorValues)
numpy.save("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontLegSensorValues.npy", frontLegSensorValues)