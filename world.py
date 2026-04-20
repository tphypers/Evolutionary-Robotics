import pybullet as p

class WORLD:
    def __init__(self, solutionID):
        #floor
        self.planeId = p.loadURDF("plane.urdf")
        #change block dynamics
        p.changeDynamics(1, -1, mass=0.1)
        p.changeDynamics(1, -1, lateralFriction=2.0) #make block stickier
        # change grabber dynamics
        p.changeDynamics(2, 11, lateralFriction=2.0)
        p.changeDynamics(2, 12, lateralFriction=2.0)

        #load world
        p.loadSDF("world" + solutionID + ".sdf")




