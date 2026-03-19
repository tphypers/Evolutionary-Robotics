# parallelHillClimber.py
from solution import SOLUTION
import constants as C
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del fitness*.txt")
        os.system("del brain*.nndf")
        
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(C.POPULATION_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(C.GENERATIONS):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].SetID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print("\n" + "-"*20)
        for i in self.parents:
            print(f'Parent {i} Fitness: {self.parents[i].fitness:.4f} | Child {i} Fitness: {self.children[i].fitness:.4f}')

    def Show_Best(self):
        best_index = 0
        for i in self.parents:
            if self.parents[i].fitness < self.parents[best_index].fitness:
                best_index = i
        
        print(f"Showing Best Robot (ID: {best_index})")
        self.parents[best_index].Start_Simulation("GUI")
        self.parents[best_index].Wait_For_Simulation_To_End()