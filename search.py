import os

for sim in range(5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")