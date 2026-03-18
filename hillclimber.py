from solution import SOLUTION
import constants as C
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        self.parent.Evaluate("GUI")

    def evolve(self):
        for currentGeneration in range(C.GENERATIONS):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Print(self):
        print(f'\nParent: {self.parent.fitness} Child: {self.child.fitness}')

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child