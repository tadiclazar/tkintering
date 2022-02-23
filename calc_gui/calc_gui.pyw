import tkinter as tk
from tkinter import ttk
import os

import buttons


def equ_event_on_ret(event, entry_var):
    """Event function. Binds the Return key to the entry widget.
    Evaluates an expression inside the entry widget."""
    buttons.equ_btn_command(entry_var)


def main():
    root = tk.Tk()
    root.wm_title("Calculator")

    style = ttk.Style()
    theme_name = "vista" if os.name == "nt" else "clam"
    style.theme_use(theme_name)

    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nesw")

    entry_var = tk.StringVar(master=frame)

    entry_w = ttk.Entry(frame, textvariable=entry_var)
    entry_w.bind('<Return>', lambda ev, ew=entry_var: equ_event_on_ret(ev, ew))
    button_l = buttons.make_digit_buttons(frame, entry_var)

    entry_w.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nesw")
    buttons.grid_buttons(button_l)

    root.mainloop()


if __name__ == '__main__':
    main()
