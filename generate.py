import pyrosim.pyrosim as pyrosim

#world creation
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name=f"Box", pos=[-2,-2,.5] , size=[1,1,1])
    pyrosim.End()

#Robot creation
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name=f"Link0", pos=[0,0,.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name=f"Link1", pos=[0,0,.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name=f"Link2", pos=[0,0,.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,.5,.5])
    pyrosim.Send_Cube(name=f"Link3", pos=[0,.5,0] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
    pyrosim.Send_Cube(name=f"Link4", pos=[0,.5,0] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,.5,-.5])
    pyrosim.Send_Cube(name=f"Link5", pos=[0,0,-.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
    pyrosim.Send_Cube(name=f"Link6", pos=[0,0,-.5] , size=[1,1,1])

    pyrosim.End()

Create_Robot()
Create_World()