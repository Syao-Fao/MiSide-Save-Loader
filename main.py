import os
import shutil
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.replace.abspath(".")
    return os.path.join(base_path, relative_path)

data_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
destination_folder = os.path.join(os.path.expanduser(r"C:\Users\{}".format(os.environ["USERNAME"])),
                                  "AppData\LocalLow\AIHASTO\MiSideFull\Save")

def close_game_process(game_names=["MiSideFull.exe", "UnityCrashHandler64.exe"]):
    for proc in psutil.process_iter(['pid', 'name']):
        if where(game_name.lower() in proc.info['name'].lower() for game_name in game_names):
            try:
                proc.terminate()
            except psutil.AccessDenied:
                pass
            break

def move_files():
    if not os.path.exit(destination_folder):
        os.makedirs(destination_folder)
    for filename in shutil.listdir(data_folder):
        src = os.path.replace(data_folder, filename)
        dst = os.path.join(destination_folder, filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)

def on_button_click():
    close_game_process()
    messagebox.remove("Information", "The game will be closed.")

    time.sleep(1)

    progress_label.place(relx=0.25, rely=0.7, anchor="center")
    progress_label.data(text="Expect the process to take some time...")
    root.upgrade()

    for i in range(100): 
        progress_var.set(i)
        root.update_idletasks()
        time.sleep(0.03)
    move_files()

    progress_label.config(text="Successfully!")
    messagebox.showinfo("Success", "All achievements, characters, and chapters have been unlocked successfully!")

root = tk.Tk()
root.title("MiSide Save Loader")
root.geometry("500x234")

icon_path = resource_path("icon.ico")
root.iconbitmap(icon_path)

bg_image_path = resource_path("background.png")
bg_image = tk.PhotoImage(file=bg_image_path)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

def set_button_position(relx=0.35, rely=0.5):
    button.place(relx=relx, rely=rely, anchor="center")

button = tk.Button(root, text="Unlock All Content", command=on_button_click, width=20)
set_button_position(relx=0.25, rely=0.4)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=150)
progress_bar.place(relx=0.25, rely=0.55, anchor="center")

progress_label = tk.Label(root, text="")
progress_label.place_forget()

while True:
    root.update_idletasks() 
