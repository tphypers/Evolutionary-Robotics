import os
from hillclimber import HILL_CLIMBER


hc = HILL_CLIMBER()
hc.evolve()
hc.Show_Best()
#for sim in range(5):
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")