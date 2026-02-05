import numpy
import matplotlib.pyplot as plot

#load data
backLegSensorValues = numpy.load("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\backLegSensorValues.npy")
frontLegSensorValues = numpy.load("C:\\Users\\26jtm\\source\\repos\\Evolutionary-Robotics\\data\\frontLegSensorValues.npy")

plot.plot(backLegSensorValues, label = "back", linewidth = 2)
plot.plot(frontLegSensorValues, label = "front", linewidth = 2)

plot.legend()
plot.show()