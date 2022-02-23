import tkinter as tk
from tkinter import ttk
import urllib.request
import os

from download_funcs import get_content, get_content_from_file


def main():
    root = tk.Tk()
    root.wm_title("Content Downloader")

    style = ttk.Style()
    if os.name == "nt":
        style.theme_use("vista")
    else:
        self.style.theme_use("clam")

    frame = ttk.Frame(root)

    help_str = tk.StringVar(frame)
    help_str.set("Enter URL to the content below."
                 "\nEnter optional path where the content will be stored."
                 "\nIf omitted, content is stored in the current folder.")

    url_entry_var = tk.StringVar(frame)
    path_var = tk.StringVar(frame)
    filen_var = tk.StringVar(frame)

    help_lbl = ttk.Label(frame, textvariable=help_str, justify=tk.CENTER)
    url_lbl = ttk.Label(frame, text="URL: ")
    path_lbl = ttk.Label(frame, text="Path: ")

    url_entry = ttk.Entry(frame, textvariable=url_entry_var, width=30)
    path_entry = ttk.Entry(frame, textvariable=path_var, width=30)

    download_btn = ttk.Button(frame, text="Download",
                              command=lambda pa_var=path_var, url_evar=url_entry_var: get_content(pa_var, url_evar), width=20)

    file_lbl = ttk.Label(frame, text="From File: ")
    file_entry = ttk.Entry(frame, textvariable=filen_var, width=40)

    from_file_btn = ttk.Button(frame, text="Get From File",
                               command=lambda fn=filen_var, pvar=path_var: get_content_from_file(fn, pvar), width=15)

    frame.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
    help_lbl.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
    url_lbl.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    path_lbl.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    url_entry.grid(row=1, column=1, padx=5, pady=5, sticky="nesw")
    path_entry.grid(row=2, column=1, padx=5, pady=5, sticky="news")
    download_btn.grid(row=3, column=1, padx=5, pady=5, sticky="sw")

    file_lbl.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
    file_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)
    from_file_btn.grid(row=5, column=1, padx=5, pady=5, sticky=tk.S)

    root.mainloop()


if __name__ == '__main__':
    main()
    urllib.request.urlcleanup()
