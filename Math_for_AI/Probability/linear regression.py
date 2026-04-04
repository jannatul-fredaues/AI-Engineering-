import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

try:
    # 1. Get user input for data points
    # Example: x = 1, 2, 3, 4, 5  |  y = 2, 4, 5, 4, 5
    x_input = input("Enter x values separated by spaces: ").split()
    y_input = input("Enter y values separated by spaces: ").split()

    # Convert to numpy arrays and reshape for the model
    X = np.array([float(i) for i in x_input]).reshape(-1, 1)
    y = np.array([float(i) for i in y_input])

    if len(X) != len(y):
        print("Error: You must have the same number of x and y values.")
    else:
        # 2. Create and train the model
        model = LinearRegression()
        model.fit(X, y)

        # 3. Output the findings
        print("-" * 30)
        print(f"Slope (m): {model.coef_[0]:.4f}")
        print(f"Intercept (b): {model.intercept_:.4f}")
        print(f"R-squared (Accuracy score): {model.score(X, y):.4f}")

        # 4. Predict a new value
        predict_val = float(input("Enter an x value to predict its y: "))
        prediction = model.predict([[predict_val]])
        print(f"Predicted y for x={predict_val}: {prediction[0]:.4f}")

except ValueError:
    print("Invalid input! Please enter only numbers.")