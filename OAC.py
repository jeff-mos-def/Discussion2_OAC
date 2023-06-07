# Values matrix
values = np.array([[2, 4, 3, 5],
                   [1, 2, 1, 3],
                   [3, 1, 2, 2]])

# Number of persons and jobs
I, J = values.shape

# Objective coefficients
c = -values.flatten()

# Equality constraints: Each person's time must be fully allocated
A_eq = np.zeros((I, I * J))
for i in range(I):
    A_eq[i, i * J: (i + 1) * J] = 1
b_eq = np.ones(I)

# Bounds for variables: x_ij >= 0
bounds = [(0, None)] * (I * J)

# Solve linear programming problem
res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

# Extract solution
x_optimal = res.x.reshape(I, J)

print("Optimal Assignment:")
print(x_optimal)
