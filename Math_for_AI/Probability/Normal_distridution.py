import math

def normal_distribution(x, mean, std_dev):
    exponent = -0.5 * ((x - mean) / std_dev) ** 2
    coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
    return coefficient * math.exp(exponent)

# Example usage
mean = 0
std_dev = 1
x = float(input("Enter the value of x: "))
probability = normal_distribution(x, mean, std_dev)
print(f"Probability density at x={x}: {probability}")