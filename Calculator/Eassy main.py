# Simple calculator using only operators and variables (no functions)

# Variables to store numbers
num1 = 10
num2 = 5

# Addition
operation = "Addition"
result = num1 + num2
print(f"{operation}: {num1} + {num2} = {result}")

# Subtraction
operation = "Subtraction"
result = num1 - num2
print(f"{operation}: {num1} - {num2} = {result}")

# Multiplication
operation = "Multiplication"
result = num1 * num2
print(f"{operation}: {num1} * {num2} = {result}")

# Division
operation = "Division"
if num2 != 0:
	result = num1 / num2
	print(f"{operation}: {num1} / {num2} = {result}")
else:
	print(f"{operation}: Division by zero error")
