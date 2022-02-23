from tkinter import ttk


def add_digit_to_entry(char, entry_var):
    """Button command that places text from buttons inside the entry.
    Requires a character and the text variable of the entry widget."""
    entry_text = entry_var.get()
    new_text = entry_text + char
    entry_var.set(new_text)


def equ_btn_command(entry_var):
    """Button command that evaluates the expression inside the entry widget.
    Takes the text variable of the entry widget as an argument."""
    expr = entry_var.get()
    if expr:
        try:
            evaluated = eval(expr)
        except SyntaxError:
            evaluated = "Invalid syntax"
        except ZeroDivisionError:
            evaluated = "Zero divisor error"

    entry_var.set(f"{evaluated}")


def make_digit_buttons(frame, entry_var):
    """Builds and returns a list of all buttons.
    Requires a frame and the text variable to the entry widget."""
    digit_chars = "7 8 9 4 5 6 1 2 3 0 + - * / % ( )".split()
    buttons = []

    for char in digit_chars:
        btn_command = lambda char=char, entry=entry_var: add_digit_to_entry(char, entry)
        btn = ttk.Button(frame, text=char, command=btn_command)
        buttons.append(btn)

    clear_btn = ttk.Button(frame, text="C", command=lambda evar=entry_var: evar.set(""))
    equ_btn = ttk.Button(frame, text="=", command=lambda: equ_btn_command(entry_var))

    buttons.append(clear_btn)
    buttons.append(equ_btn)

    return buttons


def grid_buttons(btn_l):
    """Grids the buttons to their place. Requires a list of buttons."""
    r = 1
    c = 0

    for i, btn in enumerate(btn_l):
        if i % 3 == 0:
            r += 1
        btn.grid(row=r, column=c, padx=2, pady=2, sticky="nesw")
        c += 1
        if c % 3 == 0:
            c = 0
