
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

SIMULATION(directOrGUI, solutionID).Get_Fitness()