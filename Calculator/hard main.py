# Simple GUI Calculator using Tkinter
# This calculator uses only operators and variables, no custom functions
# Comments are included for clarity

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Label to show the expression above the entry
expression_label = tk.Label(root, text="", anchor='e', width=30)
expression_label.grid(row=0, column=0, columnspan=4)

# Entry widget to display numbers and results
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=1, column=0, columnspan=4)

# Variables to store numbers and operation
num1 = None
num2 = None
operation = None
expression = ""

# Button click event
def button_click(value):
    global expression
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))
    expression += str(value)
    expression_label.config(text=expression)

# Clear entry and expression
def button_clear():
    global expression
    entry.delete(0, tk.END)
    expression = ""
    expression_label.config(text=expression)

# Set operation and first number
def button_operation(op):
    global num1, operation, expression
    try:
        num1 = float(entry.get())
        operation = op
        expression += op
        expression_label.config(text=expression)
        entry.delete(0, tk.END)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Calculate result and show expression
def button_equal():
    global num1, num2, operation, expression
    try:
        num2 = float(entry.get())
        entry.delete(0, tk.END)
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Division by zero'
        else:
            result = 'Invalid operation'
        entry.insert(0, str(result))
        expression_label.config(text=expression + "=" + str(result))
        expression = ""
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")
        expression_label.config(text="Invalid Input")
        expression = ""
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, f"Error: {e}")
        expression_label.config(text=f"Error: {e}")
        expression = ""

# Create buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('/', 5, 3),
]

for (text, row, col) in buttons:
    if text in '+-*/':
        cmd = lambda op=text: button_operation(op)
    elif text == 'C':
        cmd = button_clear
    else:
        cmd = lambda val=text: button_click(val)
    tk.Button(root, text=text, width=5, command=cmd).grid(row=row, column=col)

# Equal button
tk.Button(root, text='=', width=22, command=button_equal).grid(row=6, column=0, columnspan=4)

# Start the GUI event loop
root.mainloop()
