import tkinter as tk
from math import pi, e

# Function to initialize and run the calculator
def run_calculator():
    # Initialize the main window
    window = tk.Tk()
    window.title("Scientific Calculator")
    window.geometry("300x600")
    window.resizable(False, False)

    # Global variable for storing the current expression
    expression = ""

    # Function to update the expression in the display
    def update_expression(value):
        nonlocal expression
        expression += str(value)
        display_label.config(text=expression)

    # Function to clear the display
    def clear_display():
        nonlocal expression
        expression = ""
        display_label.config(text=expression)

    # Function to evaluate the expression
    def evaluate_expression():
        nonlocal expression
        try:
            # Evaluate the expression and update the display
            result = eval(expression)
            display_label.config(text=str(result))
            expression = str(result)  # Update expression to result
        except Exception:
            # Show error message in case of invalid input
            display_label.config(text="ERROR")
            expression = ""

    # Create the display label and place it in the grid
    display_label = tk.Label(window, text="", font=("Arial", 20), anchor="e", bg="lightgray", fg="black")
    display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Button definitions and grid configuration
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('Clear', 5, 0), ('(', 5, 1), (')', 5, 2), ('%', 5, 3),
        ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
        ('log', 7, 0), ('exp', 7, 1), ('^', 7, 2), ('pi', 7, 3),
    ]

    # Function to create buttons and add them to the grid
    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(window, text=text, font=("Arial", 18), command=evaluate_expression)
        elif text == 'Clear':
            button = tk.Button(window, text=text, font=("Arial", 18), command=clear_display)
        elif text == 'pi':
            button = tk.Button(window, text=text, font=("Arial", 18), command=lambda: update_expression(pi))
        elif text == 'exp':
            button = tk.Button(window, text=text, font=("Arial", 18), command=lambda: update_expression(e))
        elif text == '^':
            button = tk.Button(window, text=text, font=("Arial", 18), command=lambda: update_expression('**'))
        elif text in ('sin', 'cos', 'tan', 'log', 'sqrt'):
            button = tk.Button(window, text=text, font=("Arial", 18), command=lambda t=text: update_expression(t + '('))
        else:
            button = tk.Button(window, text=text, font=("Arial", 18), command=lambda t=text: update_expression(t))

        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    # Configure grid rows and columns to have equal weight
    for i in range(8):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

    # Start the Tkinter event loop
    window.mainloop()

run_calculator()