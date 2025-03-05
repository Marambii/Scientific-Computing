import sympy as sp

# Define the matrix A
A = sp.Matrix([[2, 1], [1, 3]])

# Compute AA
B = A * A 

# Compute the determinant of AA
det_B = B.det()
print(f"Determinant of AA: {det_B}")

# Find the eigenvalues of AA
eigenvals_B = B.eigenvals()
print(f"Eigenvalues of AA: {eigenvals_B}")

# Compute the characteristic equation of AA
x = sp.symbols('x')
char_eq_B = B.charpoly(x)
print(f"Characteristic equation of AA: {char_eq_B}")

# Verify that the eigenvalues satisfy the characteristic equation
for eigenval in eigenvals_B:
    assert char_eq_B.subs(x, eigenval) == 0, f"Eigenvalue {eigenval} does not satisfy the characteristic equation"

print("All eigenvalues satisfy the characteristic equation of AA.")
