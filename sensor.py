import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()
        
    def Prepare_To_Sense(self):
        self.values = numpy.zeros(c.SIM_LENGTH)

    def Get_Value(self, step):
         self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    def Save_Values(self):
        numpy.save(f"C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\{self.linkName}SensorValues.npy", self.values)




