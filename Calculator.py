import tkinter as tk

# Function to update expression in the entry field
def update_expression(entry, value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to evaluate the expression
def evaluate_expression(entry):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear_entry(entry):
    entry.delete(0, tk.END)

# Creating the main window
window = tk.Tk()
window.title("CaALCULATOR")
window.attributes("-alpha",1)
window.resizable(0,0)

# Creating an entry widget to display expressions and results
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]


for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18),
                           bg="grey",fg="white",command=lambda e=entry: evaluate_expression(e))
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18),
                           command=lambda e=entry, t=text: update_expression(e, t))
    button.grid(row=row, column=column)

# Creating a clear button
clear_button = tk.Button(window, text='C', width=5, height=2, font=('Arial', 18),
                         command=lambda e=entry: clear_entry(e))
clear_button.grid(row=4, column=4)

# Running the application
window.mainloop()

