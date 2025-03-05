import sympy as sp

# Define the symbols
s, t = sp.symbols('s t')

# Define the Laplace Transform H(s)
H_s = 1 / (s**2 + 3*s + 2)

# Factor the denominator
factored_denominator = sp.factor(s**2 + 3*s + 2)
print(f"Factored Denominator: {factored_denominator}")

# Compute the inverse Laplace Transform to find h(t)
h_t = sp.inverse_laplace_transform(H_s, s, t)
print(f"Inverse Laplace Transform h(t): {h_t}")

# Find the poles of the system
poles = sp.solve(s**2 + 3*s + 2, s)
print(f"Poles of the system: {poles}")