# 8.
# Generates one-hot encodings for an array using NumPy, where each unique value in the array corresponds to a binary encoded vector.

import numpy as np

# Define your input array with categorical values
input_array = np.array([0, 2, 1, 2, 0])

# Calculate the number of unique categories
num_categories = np.max(input_array) + 1

# Generate one-hot encodings using np.eye()
one_hot_encodings = np.eye(num_categories)[input_array]

print("Input array:")
print(input_array)

print("\nOne-hot encodings:")
print(one_hot_encodings)