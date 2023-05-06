import tkinter as tk

# Erstelle eine Instanz des Hauptfensters
root = tk.Tk()

# Ändere den Titel des Hauptfensters
root.title("Rechner")


# Erstelle ein Eingabefeld-Widget
input_field = tk.Entry(root, width=38, borderwidth=5, bg="#333", fg="#fff")
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Erstelle Schaltflächen für arithmetische Operationen
def button_equals():
    second_number = float(input_field.get())
    input_field.delete(0, tk.END)
    if math=="add":
        input_field.insert(tk.END, f_num+second_number)
    if math=="subtraction":
        input_field.insert(tk.END, f_num-second_number)
    if math=="multiplication":
        input_field.insert(tk.END, f_num*second_number)
    if math=="division":
        input_field.insert(tk.END, f_num/second_number)
def button_add():
    first_number = input_field.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_subtract():
    first_number = input_field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_multiply():
    first_number = input_field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_divide():
    first_number = input_field.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_clear():
    first_number = 0
    input_field.delete(0, tk.END)

def button_1_click():
    input_field.insert(tk.END, "1")

def button_2_click():
    input_field.insert(tk.END, "2")

def button_3_click():
    input_field.insert(tk.END, "3")

def button_4_click():
    input_field.insert(tk.END, "4")

def button_5_click():
    input_field.insert(tk.END, "5")

def button_6_click():
    input_field.insert(tk.END, "6")

def button_7_click():
    input_field.insert(tk.END, "7")

def button_8_click():
    input_field.insert(tk.END, "8")

def button_9_click():
    input_field.insert(tk.END, "9")

def button_0_click():
    input_field.insert(tk.END, "0")
def button_dot_click():
    input_field.insert(tk.END, ".")
# Erstelle Schaltflächen für Ziffern
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=button_1_click ,bg="#333", fg="#fff")
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=button_2_click ,bg="#333", fg="#fff")
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=button_3_click ,bg="#333", fg="#fff")
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=button_4_click ,bg="#333", fg="#fff")
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=button_5_click ,bg="#333", fg="#fff")
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=button_6_click ,bg="#333", fg="#fff")
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=button_7_click ,bg="#333", fg="#fff")
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=button_8_click ,bg="#333", fg="#fff")
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=button_9_click ,bg="#333", fg="#fff")
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=button_0_click ,bg="#333", fg="#fff")
button_dot = tk.Button(root, text=",", padx=40, pady=20, command=button_dot_click,bg="#333", fg="#fff")


# Erstelle Schaltflächen für arithmetische Operationen
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add,bg="#333", fg="#fff")
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract,bg="#333", fg="#fff")
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply,bg="#333", fg="#fff")
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide,bg="#333", fg="#fff")

# Erstelle eine Schaltfläche zum Löschen
button_clear = tk.Button(root, text="C", padx=40, pady=20, command=button_clear,bg="#333", fg="#fff")

# Erstelle eine Schaltfläche zum Auswerten
button_equals = tk.Button(root, text="=", padx=91, pady=20, command=button_equals,bg="#333", fg="#fff")

# Füge die Schaltflächen zum Raster hinzu
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_clear.grid(row=4, column=2)
button_equals.grid(row=5, column=0, columnspan=4)

# Starte die Hauptereignisschleife
root.mainloop()
