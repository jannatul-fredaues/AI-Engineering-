import numpy as np

# Simulation based on user input
sim_size = int(input("How many intervals should we simulate? "))
sim_data = np.random.poisson(np.lcm, sim_size)

print(f"Simulated average: {np.mean(sim_data):.2f}")
print(f"First 10 simulated counts: {sim_data[:10]}")