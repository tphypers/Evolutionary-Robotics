import os
import numpy as np
import matplotlib.pyplot as plt
from parallelHillClimber import PARALLEL_HILL_CLIMBER

NUM_RUNS = 20 

def run_experiment(body_type):
    all_curves = []
    best_overall_fitness = -np.inf
    best_overall_weights = None
    
    for r in range(NUM_RUNS):
        print(f"--- Running {body_type} Bot: Run {r+1}/{NUM_RUNS} ---")
        phc = PARALLEL_HILL_CLIMBER(body_type)
        phc.evolve()
        
        # Find the best bot in this specific run
        best_index = 0
        for i in phc.parents:
            if phc.parents[i].fitness > phc.parents[best_index].fitness:
                best_index = i
        
        run_best_bot = phc.parents[best_index]
        
        # Check if this bot is the best of ALL runs so far
        if run_best_bot.fitness > best_overall_fitness:
            best_overall_fitness = run_best_bot.fitness
            
            best_overall_weights = run_best_bot.weights.copy() 
            
        # Store the fitness curve from this run
        all_curves.append(phc.average_fitness_curve)
        
    # Save the absolute best weights to a file in your directory
    np.save(f"best_{body_type}_weights.npy", best_overall_weights)
    print(f"Finished {body_type} Bot. Best overall fitness: {best_overall_fitness}")
    
    return all_curves

# Run the experiments
curves_A = run_experiment("A")
curves_B = run_experiment("B")

# Convert to numpy arrays to easily calculate the average across columns (generations)
curves_A = np.array(curves_A)
curves_B = np.array(curves_B)

avg_curve_A = np.mean(curves_A, axis=0)
avg_curve_B = np.mean(curves_B, axis=0)

#GRAPHING
plt.figure(figsize=(10,6))

for curve in curves_A:
    plt.plot(curve, color='blue', alpha=0.15)
for curve in curves_B:
    plt.plot(curve, color='orange', alpha=0.15)
    
# Plot the averages with solid, thick lines
plt.plot(avg_curve_A, color='blue', linewidth=3, label='Average Bot A')
plt.plot(avg_curve_B, color='orange', linewidth=3, label='Average Bot B')

plt.title('Evolutionary Progress: Bot A vs Bot B')
plt.xlabel('Generation')
plt.ylabel('Average Population Fitness')
plt.legend()

# Save and show
plt.savefig('A_vs_B_fitness_comparison.png')
plt.show()