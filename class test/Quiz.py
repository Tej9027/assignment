import tkinter as tk
from tkinter import messagebox
import json


data = [
    {
        "question": "when was python invented?",
        "options": ["1991","1995","1994","1998"],
        "answer": "1991"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["tuple", "string", "list", "integer"],
        "answer": "list"
    },
    {
        "question": "What is the keyword to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What does 'len' function do in Python?",
        "options": ["Find the length", "Create a list", "Print a string", "None of the above"],
        "answer": "Find the length"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["Brackets", "Indentation", "Parentheses", "Quotes"],
        "answer": "Indentation"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["tuple", "string", "list", "integer"],
        "answer": "list"
    },
    {
        "question": "What is the keyword to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What does 'len' function do in Python?",
        "options": ["Find the length", "Create a list", "Print a string", "None of the above"],
        "answer": "Find the length"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["Brackets", "Indentation", "Parentheses", "Quotes"],
        "answer": "Indentation"
    },
    {
        "question": "What is the output of print('Hello' + 'World')?",
        "options": ["Hello World", "HelloWorld", "Hello", "World"],
        "answer": "HelloWorld"
    },
    {
        "question": "Which data type is used to store a sequence of characters in Python?",
        "options": ["list", "int", "string", "tuple"],
        "answer": "string"
    },
    {
        "question": "What is the output of the following code: print(10 // 3)?",
        "options": ["3", "3.33", "4", "3.0"],
        "answer": "3"
    },
    {
        "question": "Which method is used to add an element at the end of a list in Python?",
        "options": ["insert()", "append()", "add()", "extend()"],
        "answer": "append()"
    },
    {
        "question": "Which keyword is used for error handling in Python?",
        "options": ["error", "catch", "try", "except"],
        "answer": "try"
    },
    {
        "question": "Which of the following statements will create a dictionary in Python?",
        "options": [
            "d = {1, 2, 3}",
            "d = [1: 'one', 2: 'two']",
            "d = {'one': 1, 'two': 2}",
            "d = (1, 2, 3)"
        ],
        "answer": "d = {'one': 1, 'two': 2}"
    },
    {
        "question": "What is the output of the expression 'Python'[0:3]?",
        "options": ["Pyt", "yth", "Py", "tho"],
        "answer": "Pyt"
    },
    {
        "question": "Which of the following functions can be used to convert a string to a list of characters?",
        "options": ["list()", "char()", "str()", "split()"],
        "answer": "list()"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["int", "float", "real", "list"],
        "answer": "real"
    },
    {
        "question": "Which of the following operators is used to check if two values are not equal in Python?",
        "options": ["<>", "!=", "==", "!=="],
        "answer": "!="
    },
    {
        "question": "What will be the output of the following code: print('Python'.lower())?",
        "options": ["PYTHON", "python", "Python", "pYTHON"],
        "answer": "python"
    },
    {
        "question": "Which function is used to generate a random number in Python?",
        "options": ["randomize()", "rand()", "random()", "randint()"],
        "answer": "randint()"
    },
    {
        "question": "Which of the following is the correct way to declare a variable in Python?",
        "options": ["int a = 5;", "var a = 5;", "a = 5", "declare a = 5"],
        "answer": "a = 5"
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": [
            "Ends the loop",
            "Skips the current iteration",
            "Ends the program",
            "None of the above"
        ],
        "answer": "Ends the loop"
    },
    {
        "question": "Which of the following methods is used to remove whitespace from both ends of a string in Python?",
        "options": ["strip()", "trim()", "remove()", "delete()"],
        "answer": "strip()"
    }
]

class Quizapp:
    def __init__(self,root):
        self.root = root
        self.root.title("Python Quiz")

        self.question_index = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Times New Roman", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.selected_option, value="", font=("Arial", 14))
            button.pack(anchor="w", padx=20, pady=5)
            self.option_buttons.append(button)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=20)
        
        self.quit_button = tk.Button(root, text="Quit", command=self.root.quit, font=("Arial", 14))
        self.quit_button.pack(pady=20)
        
        self.load_question()

    def load_question(self):
        question_data = data[self.question_index]
        self.question_label.config(text=question_data["question"])
        
        self.selected_option.set(None)
        
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)
    
    def next_question(self):
        if self.selected_option.get() == data[self.question_index]["answer"]:
            self.score += 1
        
        self.question_index += 1
        
        if self.question_index < len(data):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(data)}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Quizapp(root)
    root.mainloop()
