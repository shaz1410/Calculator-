import tkinter as tk
from tkinter import messagebox
from calculator import add, subtract, multiply, divide, power, modulus

# ---------------- Calculator Logic ---------------- #
def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def calculate():
    try:
        expr = entry.get()

        if '**' in expr:
            a, b = map(float, expr.split('**'))
            result = power(a, b)
        elif '%' in expr:
            a, b = map(float, expr.split('%'))
            result = modulus(a, b)
        elif '+' in expr:
            a, b = map(float, expr.split('+'))
            result = add(a, b)
        elif '-' in expr:
            a, b = map(float, expr.split('-'))
            result = subtract(a, b)
        elif '*' in expr:
            a, b = map(float, expr.split('*'))
            result = multiply(a, b)
        elif '/' in expr:
            a, b = map(float, expr.split('/'))
            result = divide(a, b)
        else:
            result = float(expr)

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid input!")
        entry.delete(0, tk.END)

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("Pink Python Calculator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#FFC0CB")  # Light pink background

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", bg="#FFD1DC", fg="#800000")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Button layout with pink theme
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('**', 5, 1), ('←', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, bg="#FF69B4", fg="white", font=("Arial", 12),
                  command=calculate).grid(row=row, column=col, sticky="nsew")
    elif text == "C":
        tk.Button(root, text=text, width=5, height=2, bg="#FF1493", fg="white", font=("Arial", 12),
                  command=clear).grid(row=row, column=col, sticky="nsew")
    elif text == "←":
        tk.Button(root, text=text, width=5, height=2, bg="#FF69B4", fg="white", font=("Arial", 12),
                  command=backspace).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, width=5, height=2, bg="#FFC0CB", fg="#800000", font=("Arial", 12),
                  command=lambda t=text: press(t)).grid(row=row, column=col, sticky="nsew")

# Make rows and columns expand evenly
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()