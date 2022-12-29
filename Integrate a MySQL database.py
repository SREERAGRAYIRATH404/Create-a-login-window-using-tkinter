import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Replace this with your own database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "login_database"

def check_credentials(username, password):
    # Connect to the database
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()

    # Execute a SQL query to retrieve the stored username and password for the given username
    cursor.execute("SELECT username, password FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()

    # If no matching username was found, display an error message
    if result is None:
        messagebox.showerror("Login Error", "Invalid username or password")
    else:
        stored_username, stored_password = result

        # Check if the entered password matches the stored password
        if password == stored_password:
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login
