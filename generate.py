import pyrosim.pyrosim as pyrosim



pyrosim.Start_SDF("boxes.sdf")
for i in range(5):
    for y in range(5):
        dim = 1
        for x in range(10):
            pyrosim.Send_Cube(name=f"Box{i}{y}{x}", pos=[i+.5,y+.5,x+.5] , size=[dim,dim,dim])
            dim = dim * .9

pyrosim.End()
