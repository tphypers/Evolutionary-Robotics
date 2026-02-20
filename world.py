import pybullet as p

class WORLD:
    def __init__(self):
        #floor
        self.planeId = p.loadURDF("plane.urdf")
        #load world
        p.loadSDF("world.sdf")




