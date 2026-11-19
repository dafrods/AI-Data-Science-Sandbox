import numpy as np

# Number of test divisions
num_divisions = 100

# Generate a series of random numbers for testing
np.random.seed(0)
test_numbers = np.random.uniform(1, 10, num_divisions)

# Constants for fixed-point representation
FIXED_POINT_SCALE = 2**4  # 4 fractional bits

# Functions for fixed-point arithmetic
def fixed_point_divide(a, b):
    a_fixed = int(a * FIXED_POINT_SCALE)
    b_fixed = int(b * FIXED_POINT_SCALE)
    if b_fixed == 0:
        return 0
    result_fixed = a_fixed // b_fixed
    return result_fixed / FIXED_POINT_SCALE

# Functions for floating-point arithmetic
def floating_point_divide(a, b):
    return np.float16(a) / np.float16(b)

# Perform the test
fixed_point_errors = []
floating_point_errors = []

for num in test_numbers:
    true_result = num / 3  # Using 3 as the divisor for the test
    
    fixed_point_result = fixed_point_divide(num, 3)
    floating_point_result = floating_point_divide(num, 3)
    
    fixed_point_error = abs(true_result - fixed_point_result)
    floating_point_error = abs(true_result - floating_point_result)
    
    fixed_point_errors.append(fixed_point_error)
    floating_point_errors.append(floating_point_error)

# Calculate cumulative errors
total_fixed_point_error = sum(fixed_point_errors)
total_floating_point_error = sum(floating_point_errors)

print((total_fixed_point_error, total_floating_point_error))
