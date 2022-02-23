from threading import Thread
import urllib.request
import os

import tkinter as tk
from tkinter import messagebox


def get_content(path_var, url_entry_var):
    url = url_entry_var.get()
    path = path_var.get()

    sep = "\\" if os.name == "nt" else "/"
    error = "URL is in wrong format!"
    file_name = url.strip().split("/")[-1]

    if not url.startswith("http"):
        messagebox.showerror(title="URL Error", message=error)
        return None

    if not path:
        t = Thread(target=urllib.request.urlretrieve, args=(url, file_name))
    else:
        if os.name == "nt":
            path = path.replace("\\", "\\\\")

        if sep == path[-1]:
            t = Thread(target=urllib.request.urlretrieve, args=(url, path + file_name))
        else:
            t = Thread(target=urllib.request.urlretrieve, args=(url, path + sep + file_name))

    t.start()


def start_file_tasks(tasks):
    for task in tasks:
        task.start()


def get_content_from_file(filen_var, path_var):
    tasks = []
    file_name = filen_var.get()
    path = path_var.get()
    sep = "\\" if os.name == "nt" else "/"

    max_lines = 10

    if path and os.name == "nt":
        path = path.replace("\\", "\\\\")

    try:
        with open(file_name) as content:
            lines = content.readlines()

            if len(lines) > max_lines:
                messagebox.showerror(title="Max Lines Error", message=f"Too many lines in {file_name}! Max is {max_lines}.")
                return None

            for line in lines:
                if not line.startswith("http"):
                    continue
                content_name = line.strip().split("/")[-1]

                if path:
                    if sep == path[-1]:
                        task = Thread(target=urllib.request.urlretrieve, args=(line, path + content_name))
                    else:
                        task = Thread(target=urllib.request.urlretrieve, args=(line, path + sep + content_name))
                else:
                    task = Thread(target=urllib.request.urlretrieve, args=(line, content_name))
                tasks.append(task)

    except FileNotFoundError:
        messagebox.showerror(title="File Error", message=f"File {file_name} not found!")
        return None

    if tasks:
        start_file_tasks(tasks)