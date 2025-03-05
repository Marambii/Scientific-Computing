from sympy import symbols, Mod, Pow, mod_inverse

# Define symbols
P, e, N = symbols('P e N')

# Define the encryption function
C = Mod(Pow(P, e), N)
print("Encryption function:", C)

# Given values
P_val = 7
e_val = 3
N_val = 33

# Compute ciphertext C = P^e mod N
C_val = pow(P_val, e_val, N_val)
print("Ciphertext (C):", C_val)

# Compute modular inverse of P (if it exists)
try:
    mod_inv_P = mod_inverse(P_val, N_val)
    print("Modular inverse of P:", mod_inv_P)
except ValueError:
    print("Modular inverse does not exist.")
