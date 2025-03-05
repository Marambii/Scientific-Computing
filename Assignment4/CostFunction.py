import sympy as sp

# Define the variable and the cost function
x = sp.symbols('x')
C = 5*x**3 - 10*x**2 + 4*x + 3

# Find the symbolic derivative of C(x)
C_prime = sp.diff(C, x)
print(f"The derivative of C(x) is: {C_prime}")

# Solve for x when the cost is minimized (i.e., when the derivative is zero)
critical_points = sp.solve(C_prime, x)
print(f"Critical points: {critical_points}")

# Evaluate the second derivative to determine if the critical points are minima
C_double_prime = sp.diff(C_prime, x)
min_points = [point for point in critical_points if C_double_prime.subs(x, point) > 0]
print(f"Points where the cost is minimized: {min_points}")

# Interpret the result
if min_points:
    min_cost = C.subs(x, min_points[0])
    print(f"The cost is minimized when x = {min_points[0]}, with a minimum cost of {min_cost}")
else:
    print("No minimum cost found.")