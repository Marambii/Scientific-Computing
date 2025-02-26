def is_even(number):
    return number % 2 == 0

# Ask the user for an integer input and check if the number is even or odd
user_input = int(input("Enter an integer: "))
if is_even(user_input):
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")

# Use a for loop to generate a list of even numbers from 1 to 50 and print the list
even_numbers = [num for num in range(1, 51) if is_even(num)]
print("Even numbers from 1 to 50:", even_numbers)

# Use a while loop to print numbers from 10 down to 1 in reverse order
count = 10
while count > 0:
    print(count)
    count -= 1