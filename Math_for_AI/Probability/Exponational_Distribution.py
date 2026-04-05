import math
def exponential_distribution(x, rate):
    if x < 0:
        return 0  # Exponential distribution is defined for x >= 0
    return rate * math.exp(-rate * x)