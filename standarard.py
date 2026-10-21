import numpy as np

X = np.array([5, 7, 9, 11, 13])

# Calculate mean
mean = np.mean(X)

# Calculate squared differences
V = []
for val in X:
    V.append(int((val - mean) ** 2))


variance = np.mean(V)
SD = np.sqrt(variance)

# display results
print("values:",X)
print("Mean:", mean)
print("Variance list:", V)
print("Variance:", variance)
print(f"Standard deviation: {SD:.2f}")
