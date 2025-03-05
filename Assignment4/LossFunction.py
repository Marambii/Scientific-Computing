from sympy import symbols, diff, solve

# Define the variable and the loss function
x = symbols('x')
L = 3*x**2 + 2*x - 5

# Compute the first derivative (gradient)
gradient = diff(L, x)
print(f"First derivative (gradient): {gradient}")

# Solve for x when the gradient is zero (optimal solution)
optimal_x = solve(gradient, x)
print(f"Optimal solution (x): {optimal_x}")

# Compute the second derivative
L_double_prime = diff(gradient, x)
print(f"Second derivative: {L_double_prime}")

# Check if it is a minimum or maximum
for val in optimal_x:
    second_derivative_value = L_double_prime.subs(x, val)
    if second_derivative_value > 0:
        print(f"x = {val} is a minimum")
    elif second_derivative_value < 0:
        print(f"x = {val} is a maximum")
    else:
        print(f"x = {val} is a point of inflection")