"""Fill json template with data from tk GUI"""
import tkinter as tk
from tkinter import ttk

from sqlearning.json import save_json_data

if __name__ == '__main__':

    # Main application window
    root = tk.Tk()
    root.title("Fill JSON Template")

    # Widgets for each field in the JSON template
    title_label = tk.Label(root, text="Title:")
    title_label.grid(row=0, column=0)
    title_var = tk.StringVar()
    title_entry = tk.Entry(root, textvariable=title_var)
    title_entry.grid(row=0, column=1)

    # Add more widgets for other fields in the JSON template...

    # Create a button to save the filled JSON data
    save_button = ttk.Button(root, text="Save", command=save_json_data)
    save_button.grid(row=99, column=0, columnspan=2)

    # Start the main event loop
    root.mainloop()
