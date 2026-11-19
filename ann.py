import numpy as np

# Given data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
              21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
y = np.array([2.1, 3.9, 5.8, 7.8, 10.1, 11.9, 14.0, 16.3, 18.2, 20.4, 22.1, 24.2, 
              26.1, 28.3, 30.4, 32.2, 34.3, 36.1, 38.2, 40.0, 42.1, 44.2, 46.0, 
              48.3, 50.1, 52.2, 54.0, 56.3, 58.2, 60.4])

# Initial values
i = 20
m = 36
q = 0.000001

# Function to compute the loss
def compute_loss(i, m, x, y):
    return np.sum((y - (i + m * x))**2)

# Function to compute the gradients
def compute_gradients(i, m, x, y):
    n = len(y)
    L_i = -2 * np.sum(y - (i + m * x))
    L_m = -2 * np.sum(x * (y - (i + m * x)))
    return L_i, L_m

# Gradient descent loop
loss = compute_loss(i, m, x, y)
steps = 0

while loss >= 1:
    steps += 1
    L_i, L_m = compute_gradients(i, m, x, y)
    i -= q * L_i
    m -= q * L_m
    loss = compute_loss(i, m, x, y)

print(f"Steps taken: {steps}")
print(f"Final Loss: {loss}")
print(f"Final intercept (i): {i}")
print(f"Final slope (m): {m}")
