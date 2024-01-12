import tkinter as tk
from tkinter import messagebox
import argparse
from pathlib import Path

from compass.unpacker.unpacker import Unpacker

def run():
    print("Run function is called.")
    root_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()

    #check if the input folders are filled
    if not root_folder or not output_folder:
        messagebox.showerror("ERROR", "Please provide the gamedata path in the first input box and the output path in the second box")
        return

    
    
    #create an instance of Unpacker with input and output folders
    unpacker = Unpacker(Path(root_folder), output_folder)
    unpacker.unpack()

def get_input_gamedata_folder():
    user_input = input_folder_entry.get()
    result_label_input.config(text=f"User Input: {user_input}")

def get_input_outputfolder():
    user_input = output_folder_entry.get()
    result_label_output.config(text=f"User Input: {user_input}")
    

#create main window
root =tk.Tk()
root.title("Compass")

# Create and pack GUI elements
label = tk.Label(root, text="Run Command")         #label
label.pack()

root.geometry("400x300")  #sizes the window

input_folder_entry = tk.Entry(root, width=50)       #to create and size the next element
input_folder_entry.pack(pady=10)

result_label_input = tk.Label(root, text="input the location of gamedata")  #label underneath the submit button
result_label_input.pack()

output_folder_entry = tk.Entry(root, width=50)       #to create and size the next element
output_folder_entry.pack(pady=10)

result_label_output = tk.Label(root, text="input the location where files will be outputed")  #label underneath the submit button
result_label_output.pack()

run_button = tk.Button(root, text="Run Command", command=run)    #the run command button
run_button.pack()
# Run main loop
root.mainloop()