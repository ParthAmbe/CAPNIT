import tkinter as tk
from tkinter import messagebox

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to change button color on hover
def on_enter(event):
    event.widget['bg'] = event.widget.hover_color

def on_leave(event):
    event.widget['bg'] = event.widget.default_color


root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")
root.config(bg='#2b2b2b')


entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10)
entry.config(bg='#e0e0e0', fg='#000000')


button_settings = {
    'font': ('Arial', 18),
    'relief': 'raised',
    'borderwidth': 2,
}


digit_color = "#f7c8c4" 
operator_color = "#fdcf58"
equal_color = "#65c18c" 
clear_color = "#f2545b" 


digit_hover = "#ffc1c1"
operator_hover = "#f0c542"
equal_hover = "#4dbf72"
clear_hover = "#e35b5b"


buttons = [
    ('7', digit_color, digit_hover, 1, 0, 1, 1), ('8', digit_color, digit_hover, 1, 1, 1, 1), ('9', digit_color, digit_hover, 1, 2, 1, 1), ('/', operator_color, operator_hover, 1, 3, 1, 1),
    ('4', digit_color, digit_hover, 2, 0, 1, 1), ('5', digit_color, digit_hover, 2, 1, 1, 1), ('6', digit_color, digit_hover, 2, 2, 1, 1), ('*', operator_color, operator_hover, 2, 3, 1, 1),
    ('1', digit_color, digit_hover, 3, 0, 1, 1), ('2', digit_color, digit_hover, 3, 1, 1, 1), ('3', digit_color, digit_hover, 3, 2, 1, 1), ('-', operator_color, operator_hover, 3, 3, 1, 1),
    ('0', digit_color, digit_hover, 4, 0, 1, 2), ('+', operator_color, operator_hover, 4, 2, 1, 1),
    ('C', clear_color, clear_hover, 4, 3, 1, 1), ('=', equal_color, equal_hover, 5, 0, 1, 4)
]


for (button_text, button_color, hover_color, row, col, rowspan, colspan) in buttons:
    b = tk.Button(root, text=button_text, **button_settings, width=6 if colspan == 1 else 14, height=2, bg=button_color)
    b.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=5, pady=5)

    b.default_color = button_color
    b.hover_color = hover_color

    if button_text == "=":
        b.bind('<Button-1>', lambda event: calculate())
    elif button_text == "C":
        b.bind('<Button-1>', lambda event: clear())
    else:
        b.bind('<Button-1>', click)

    
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)


root.mainloop()
