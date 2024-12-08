import os
import time
import tkinter as tk
from tkinter import messagebox
import webbrowser


def schedule_action(action, delay, url=None):
    """
    Schedules a system action after the specified delay in seconds.
    """
    time.sleep(delay)
    if action == "shutdown":
        if os.name == 'nt':  # For Windows
            os.system("shutdown /s /t 1")
        elif os.name == 'posix':  # For Linux/Mac
            os.system("shutdown -h now")
    elif action == "restart":
        if os.name == 'nt':  # For Windows
            os.system("shutdown /r /t 1")
        elif os.name == 'posix':  # For Linux/Mac
            os.system("shutdown -r now")
    elif action == "sleep":
        if os.name == 'nt':  # For Windows
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif os.name == 'posix':  # For Linux/Mac
            os.system("pmset sleepnow")
    elif action == "open_url":
        if url:
            webbrowser.open(url)


def start_timer(action, time_value, time_unit, url=None):
    """
    Starts the timer based on user input and action.
    """
    try:
        if not time_value:  # Check if time is not entered
            messagebox.showerror("Input Error", "Please enter a valid time value.")
            return
        
        if action == "open_url" and (not url or url.strip() == ""):  # Check if URL is required and entered
            messagebox.showerror("Input Error", "Please enter a valid URL.")
            return
        
        # Convert time to seconds
        if time_unit == "sec":
            delay = time_value
        elif time_unit == "min":
            delay = time_value * 60
        elif time_unit == "hour":
            delay = time_value * 3600

        # Confirmation dialog
        if messagebox.askyesno("Confirmation", f"Are you sure you want to {action} in {time_value} {time_unit}(s)?"):
            messagebox.showinfo("Timer Set", f"The system will {action} in {time_value} {time_unit}(s).")
            root.after(100, schedule_action, action, delay, url)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid time value.")


def create_rounded_rectangle(canvas, x1, y1, x2, y2, r, **kwargs):
    """
    Creates a rectangle with rounded corners on a canvas.
    """
    points = [
        (x1 + r, y1), (x1 + r, y1),  # Top-left corner
        (x2 - r, y1), (x2 - r, y1),  # Top-right corner
        (x2, y1 + r), (x2, y1 + r),
        (x2, y2 - r), (x2, y2 - r),  # Bottom-right corner
        (x2 - r, y2), (x2 - r, y2),
        (x1 + r, y2), (x1 + r, y2),  # Bottom-left corner
        (x1, y2 - r), (x1, y2 - r),
        (x1, y1 + r), (x1, y1 + r)
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


def create_action_button(action, column, logo_path):
    """
    Creates a section with logo, time input, and a start button for each action.
    """
    # Create a canvas for the rounded rectangle
    canvas = tk.Canvas(root, width=180, height=280, bg="#d4f1f9", highlightthickness=0)
    canvas.grid(row=2, column=column, padx=20, pady=10)
    create_rounded_rectangle(canvas, 10, 10, 170, 270, 20, fill="#f4a261", outline="#f4a261")

    # Place widgets over the canvas
    logo = tk.PhotoImage(file=logo_path)  # Load logo image
    logo_label = tk.Label(canvas, image=logo, bg="#f4a261")
    logo_label.image = logo  # Keep reference to the image
    logo_label.place(x=50, y=20)

    # Adjusted spacing for "Enter time" text
    time_label = tk.Label(canvas, text="Enter time:", bg="#f4a261", fg="#264653")
    time_label.place(x=30, y=90)

    time_entry = tk.Entry(canvas, bg="#ffffff", fg="#264653", highlightbackground="#e9c46a", relief="flat")
    time_entry.place(x=30, y=120, width=120)

    time_unit_var = tk.StringVar(value="min")
    time_unit_menu = tk.OptionMenu(canvas, time_unit_var, "sec", "min", "hour")
    time_unit_menu.configure(bg="#f4a261", fg="#264653", relief="flat")
    time_unit_menu.place(x=50, y=150)

    url_entry = None
    if action == "open_url":
        url_label = tk.Label(canvas, text="Enter URL:", bg="#f4a261", fg="#264653")
        url_label.place(x=30, y=190)

        url_entry = tk.Entry(canvas, bg="#ffffff", fg="#264653", highlightbackground="#e9c46a", relief="flat")
        url_entry.place(x=30, y=210, width=120)

    start_button = tk.Button(
        canvas,
        text="Start Timer",
        command=lambda: [
            start_timer(
                action,
                int(time_entry.get()) if time_entry.get().isdigit() else None,
                time_unit_var.get(),
                url_entry.get() if action == "open_url" else None,
            ),
            time_entry.delete(0, tk.END),  # Clear time entry after clicking
            url_entry.delete(0, tk.END) if url_entry else None,  # Clear URL entry if present
        ],
        bg="#2a9d8f",
        fg="#ffffff",
        activebackground="#37b9a3",
        activeforeground="#ffffff",
        relief="flat",
    )
    start_button.place(x=50, y=240, width=80)


# GUI Setup
root = tk.Tk()
root.title("System Action Scheduler")
root.geometry("880x400")
root.configure(bg="#d4f1f9")

# Heading
heading = tk.Label(root, text="System Action Scheduler", font=("Arial", 16), bg="#264653", fg="#ffffff")
heading.grid(row=0, column=0, columnspan=4, pady=20)

# Add extra spacing between heading and buttons
root.grid_rowconfigure(1, minsize=20)

# Create action sections
create_action_button("restart", 0, "./restart.png")  # Replace with actual path to the restart logo
create_action_button("shutdown", 1, "./shutdown.png")  # Replace with actual path to the shutdown logo
create_action_button("sleep", 2, "./sleep.png")  # Replace with actual path to the sleep logo
create_action_button("open_url", 3, "./url.png")  # Replace with actual path to the URL logo

# Run the app
root.mainloop()
