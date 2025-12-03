import tkinter as tk

def add_to_input(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")
root.config(bg="#1e1e1e")  

entry = tk.Entry(root, font=("Arial", 24), border=0, relief=tk.FLAT, justify="right", bg="#2b2b2b", fg="white")
entry.pack(fill="both", padx=20, pady=20, ipady=15)

def create_button(text, row, col):
    return tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        bg="#333333",
        fg="white",
        activebackground="#444",
        border=0,
        command=lambda: add_to_input(text)
    ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

for i in range(4):
    frame.columnconfigure(i, weight=1)
for i in range(5):
    frame.rowconfigure(i, weight=1)

buttons = [
    ("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
    ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
    ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
    ("0",3,0), (".",3,1), ("=",3,2), ("+",3,3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(frame, text="=", font=("Arial", 18), bg="#00aaff",
                  fg="white", border=0, command=calculate
                  ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        create_button(text, row, col)

tk.Button(frame, text="C", font=("Arial", 18), bg="#ff4444",
          fg="white", border=0, command=clear
          ).grid(row=4, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

root.mainloop()