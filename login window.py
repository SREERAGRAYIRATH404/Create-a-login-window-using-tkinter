import tkinter as tk
from tkinter import messagebox

def check_credentials(username, password):
    # Open the file containing the stored username and password
    with open("credentials.txt", "r") as f:
        stored_username = f.readline().strip()
        stored_password = f.readline().strip()
    
    # Check if the entered credentials match the stored credentials
    if username == stored_username and password == stored_password:
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Create the main window
window = tk.Tk()
window.title("Login")

# Create the input fields for username and password
tk.Label(window, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

tk.Label(window, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

# Create the login button
login_button = tk.Button(window, text="Login", command=lambda: check_credentials(username_entry.get(), password_entry.get()))
login_button.grid(row=2, column=1)

window.mainloop()
