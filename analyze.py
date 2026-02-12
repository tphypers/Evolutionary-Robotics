import numpy
import matplotlib.pyplot as plot

#load data
#backLegSensorValues = numpy.load("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backLegSensorValues.npy")
#frontLegSensorValues = numpy.load("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontLegSensorValues.npy")
frontTargetAngles = numpy.load("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontTargetAngles.npy")
backTargetAngles = numpy.load("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backTargetAngles.npy")

#plot.plot(backLegSensorValues, label = "back", linewidth = 2)
#plot.plot(frontLegSensorValues, label = "front", linewidth = 4)
plot.plot(frontTargetAngles, label = "front", linewidth = 6)
plot.plot(backTargetAngles, label = "back", linewidth = 1)

plot.legend()
plot.show()