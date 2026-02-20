import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.prepare_to_act()

    def prepare_to_act(self):
        self.values = numpy.zeros(c.SIM_LENGTH)
        self.amplitude = c.FRONT_AMPLITUDE
        self.frequency = c.FRONT_FREQUENCY
        if self.jointName == b'Torso_FrontLeg':
            self.frequency = self.frequency * .5
            print('BUTT')
        self.offset = c.FRONT_PHASE_OFFSET
        self.valuespre = ((numpy.linspace(0, c.TAU, c.SIM_LENGTH)))
        self.TargetAngles = self.amplitude * numpy.sin(self.frequency * self.valuespre + self.offset)
        

    def Set_Value(self, robot, step):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.TargetAngles[step],
                maxForce = c.BACK_FORCE)

    def Save_Values(self):
        numpy.save(f"C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\{self.jointName}SensorValues.npy", self.TargetAngles)
        

