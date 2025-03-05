from sympy import diff, symbols, det, integrate

x = symbols('x')
y = symbols('y')
diff_expre = diff(x**2 + 2*x + 1, x)
print("Differentiation of x^2 + 2x + 1:", diff_expre)
