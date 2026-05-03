import sys
import numpy as np
from solution import SOLUTION

if len(sys.argv) < 2:
    print("Please specify bot type: python play_best.py A   OR   python play_best.py B")
    sys.exit()

bot_type = sys.argv[1].upper()

print(f"Loading best {bot_type} bot...")

best_bot = SOLUTION(0, bot_type)

try:
    best_bot.weights = np.load(f"best_{bot_type}_weights.npy")
except FileNotFoundError:
    print(f"Could not find best_{bot_type}_weights.npy. Did you run search.py first?")
    sys.exit()

# Run in GUI mode
best_bot.Start_Simulation("GUI")
best_bot.Wait_For_Simulation_To_End()

print(f"Final Fitness: {best_bot.fitness}")