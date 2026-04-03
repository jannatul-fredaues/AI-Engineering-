import statistics

# User input
data = list(map(int, input("Enter numbers: ").split()))

# Sample standard deviation
std_dev = statistics.stdev(data)

# Population standard deviation
std_dev_pop = statistics.pstdev(data)

print("Sample Standard Deviation:", std_dev)
print("Population Standard Deviation:", std_dev_pop)