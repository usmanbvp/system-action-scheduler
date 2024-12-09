import os
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import sys
import threading

# Function to handle resource paths
def resource_path(relative_path):
    """Get the path to the resource, works for dev and PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Schedule action (Runs in a separate thread)
def schedule_action(action, delay, url=None):
    time.sleep(delay)
    
    # Handle different actions based on selected action
    if action == "shutdown":
        if os.name == "nt":
            os.system("shutdown /s /f /t 1")  # Force shutdown on Windows
        else:
            os.system("shutdown -h now")  # Shutdown on macOS/Linux
    elif action == "restart":
        if os.name == "nt":
            os.system("shutdown /r /f /t 1")  # Force restart on Windows
        else:
            os.system("shutdown -r now")  # Restart on macOS/Linux
    elif action == "sleep":
        if os.name == "nt":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Sleep on Windows
        else:
            os.system("pmset sleepnow")  # Sleep on macOS
    elif action == "open_url" and url:
        webbrowser.open(url)  # Open URL in default browser

# Start timer (Runs asynchronously in a separate thread)
def start_timer(action, time_value, time_unit, url=None):
    try:
        if not time_value:
            messagebox.showerror("Input Error", "Please enter a valid time value.")
            return
        if action == "open_url" and (not url or url.strip() == ""):
            messagebox.showerror("Input Error", "Please enter a valid URL.")
            return

        # Calculate delay in seconds based on the time unit
        if time_unit == "Sec":
            delay = time_value
        elif time_unit == "Min":
            delay = time_value * 60
        elif time_unit == "Hour":
            delay = time_value * 3600
        else:
            delay = 0  # Invalid time unit (this shouldn't happen)
        
        # Show confirmation dialog before scheduling the action
        if messagebox.askyesno("Confirmation", f"Are you sure you want to {action} in {time_value} {time_unit}(s)?"):
            # Run the action in a separate thread to avoid blocking the UI
            threading.Thread(target=schedule_action, args=(action.lower(), delay, url)).start()
            root.after(0, clear_fields)  # Clear the fields after starting the timer
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values.")

# Clear input fields
def clear_fields():
    time_entry.delete(0, tk.END)  # Clear the time entry field
    url_entry.delete(0, tk.END)  # Clear the URL entry field if visible

# Update icon based on dropdown selection
def update_icon(action):
    action_icon.config(file=resource_path(f"{action.lower()}.png"))

# GUI Setup
root = tk.Tk()
root.title("System Action Scheduler")
root.geometry("700x450")
root.configure(bg="#d4f1f9")

# Header
heading = tk.Label(root, text="System Action Scheduler", font=("Arial", 20, "bold"), bg="#264653", fg="#ffffff")
heading.pack(pady=20, fill="x")

# Unified Action Card
card_frame = tk.Frame(root, bg="#f4a261", relief="flat", bd=0)
card_frame.pack(pady=20, padx=40, fill="x")

# Dropdown for actions
action_label = tk.Label(card_frame, text="Choose Action:", bg="#f4a261", fg="#264653", font=("Arial", 12))
action_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

action_var = tk.StringVar(value="restart")
action_dropdown = ttk.Combobox(card_frame, textvariable=action_var, values=["restart", "shutdown", "sleep", "open_url"])
action_dropdown.grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")
action_dropdown.bind("<<ComboboxSelected>>", lambda e: update_icon(action_var.get()))

# Icon for selected action
action_icon = tk.PhotoImage(file=resource_path("restart.png"))
icon_label = tk.Label(card_frame, image=action_icon, bg="#f4a261")
icon_label.grid(row=1, column=0, columnspan=3, pady=10)

# Instructional text before time input
instruction_label = tk.Label(card_frame, text="The above action will be performed after the following time:", bg="#f4a261", fg="#264653", font=("Arial", 12))
instruction_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="w")

# Time input and dropdown aligned horizontally
time_label = tk.Label(card_frame, text="Enter Time:", bg="#f4a261", fg="#264653", font=("Arial", 12))
time_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")

time_entry = tk.Entry(card_frame, bg="#ffffff", fg="#264653")
time_entry.grid(row=3, column=1, padx=(5, 5), pady=5, sticky="w")

time_unit_var = tk.StringVar(value="min")
time_unit_dropdown = ttk.Combobox(card_frame, textvariable=time_unit_var, values=["Sec", "Min", "Hour"])
time_unit_dropdown.grid(row=3, column=2, padx=(5, 10), pady=5, sticky="w")

# URL input (only for open_url)
url_label = tk.Label(card_frame, text="Enter URL:", bg="#f4a261", fg="#264653", font=("Arial", 12))
url_entry = tk.Entry(card_frame, bg="#ffffff", fg="#264653")

# URL entry visibility control
def toggle_url_field(*args):
    if action_var.get().lower() == "open_url":  # Make sure comparison is case-insensitive
        url_label.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="w")  # Display the URL label
        url_entry.grid(row=4, column=1, columnspan=2, padx=(5, 10), pady=5, sticky="w")  # Display the URL entry
    else:
        url_label.grid_remove()  # Remove the URL label
        url_entry.grid_remove()  # Remove the URL entry

action_var.trace("w", toggle_url_field)  # Attach the trace function to the action dropdown

# Start button
start_button = tk.Button(card_frame, text="Start Timer", bg="#2a9d8f", fg="#ffffff", font=("Arial", 12, "bold"),
                         command=lambda: start_timer(action_var.get(), int(time_entry.get()) if time_entry.get().isdigit() else None, time_unit_var.get(), url_entry.get()))
start_button.grid(row=5, column=0, columnspan=3, pady=20)

# Run app
root.mainloop()
