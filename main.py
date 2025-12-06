import tkinter as tk
current_theme = "dark"

themes = {
    "dark": {
        "bg": "#1e1e1e",
        "entry_bg": "#2b2b2b",
        "entry_fg": "white",
        "btn_bg": "#333333",
        "btn_fg": "white",
        "btn_active": "#444",
        "eq_bg": "#00aaff",
        "clear_bg": "#ff4444",
        "toggle_fg": "white"
    },
    "light": {
        "bg": "#f2f2f2",
        "entry_bg": "white",
        "entry_fg": "black",
        "btn_bg": "#e0e0e0",
        "btn_fg": "black",
        "btn_active": "#d5d5d5",
        "eq_bg": "#4da6ff",
        "clear_bg": "#ff6666",
        "toggle_fg": "black"
    }
}

root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x450")

top_frame = tk.Frame(root)
top_frame.pack(fill="x", pady=5, padx=10)

toggle_btn = tk.Button(
    top_frame,
    text="🌙 Gelap",  
    font=("Arial", 12),
    command=lambda: toggle_theme(),
    border=0,
    relief=tk.FLAT,
    anchor="e"
)
toggle_btn.pack(side="right")

entry = tk.Entry(root, font=("Arial", 24), border=0, relief=tk.FLAT,
                 justify="right")
entry.pack(fill="both", padx=20, pady=20, ipady=15)

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

all_buttons = []

def apply_theme(theme):
    t = themes[theme]

    root.config(bg=t["bg"])
    top_frame.config(bg=t["bg"])
    frame.config(bg=t["bg"])

    entry.config(bg=t["entry_bg"], fg=t["entry_fg"])

    toggle_btn.config(
        bg=t["bg"],
        fg=t["toggle_fg"],
        activebackground=t["bg"],
        text=("🌞 Terang" if theme == "light" else "🌙 Gelap")
    )
    
    for btn in all_buttons:
        text = btn["text"]
        if text == "=":
            btn.config(bg=t["eq_bg"], fg="white")
        elif text == "C":
            btn.config(bg=t["clear_bg"], fg="white")
        else:
            btn.config(bg=t["btn_bg"], fg=t["btn_fg"], activebackground=t["btn_active"])


def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme(current_theme)

def add_to_input(value):
    entry.insert("end", value)

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

def create_button(text, row, col):
    btn = tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        border=0,
        command=lambda: add_to_input(text)
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    all_buttons.append(btn)
    return btn

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
        btn = tk.Button(
            frame, text="=", font=("Arial", 18),
            border=0, command=calculate
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        all_buttons.append(btn)
    else:
        create_button(text, row, col)

clear_btn = tk.Button(frame, text="C", font=("Arial", 18),
                      border=0, command=clear)
clear_btn.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
all_buttons.append(clear_btn)

apply_theme("dark")

root.mainloop()
