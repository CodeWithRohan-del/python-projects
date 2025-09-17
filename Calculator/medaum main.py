# Calculator using function, if, error handling, user input, and user command

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Error: Division by zero"
	return a / b

def median(a, b):
	nums = [a, b]
	nums.sort()
	if len(nums) % 2 != 0:
		return nums[len(nums)//2]
	else:
		return (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2

try:
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	command = input("Enter operation (add, subtract, multiply, divide, median): ").strip().lower()
	if command == "add":
		print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
	elif command == "subtract":
		print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
	elif command == "multiply":
		print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
	elif command == "divide":
		print(f"Division: {num1} / {num2} = {divide(num1, num2)}")
	elif command == "median":
		print(f"Median of {num1} and {num2} is {median(num1, num2)}")
	else:
		print("Error: Unknown operation. Please enter add, subtract, multiply, divide, or median.")
except ValueError:
	print("Error: Please enter valid numbers.")
