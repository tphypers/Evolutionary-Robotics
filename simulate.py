import pybullet as p
import time
import pybullet_data

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

#running simulation world for a few seconds
for i in range(1000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)
p.disconnect()