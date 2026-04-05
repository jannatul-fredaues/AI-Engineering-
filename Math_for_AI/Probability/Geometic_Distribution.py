from scipy.stats import geom

try:
    # 1. Get user inputs
    p = float(input("Enter the probability of success (p) [0 to 1]: "))
    k = int(input("Enter the trial number for the first success (k): "))

    if not (0 < p <= 1):
        print("Error: Probability (p) must be greater than 0 and less than or equal to 1.")
    elif k < 1:
        print("Error: The trial number (k) must be at least 1.")
    else:
        # 2. Calculate results
        # Probability that the FIRST success happens exactly on trial k
        pmf_val = geom.pmf(k, p)
        
        # Probability that it takes k or fewer trials to get a success
        cdf_val = geom.cdf(k, p)

        # 3. Output results
        print("-" * 30)
        print(f"Results for p={p}, k={k}:")
        print(f"Prob. that first success is exactly on trial {k}: {pmf_val:.6f}")
        print(f"Prob. of getting a success within {k} trials: {cdf_val:.6f}")

except ValueError:
    print("Invalid input! Please enter a decimal for p and an integer for k.")