import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create the table to store the username and password
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY NOT NULL,
             password TEXT NOT NULL);''')

# Create the login window
def login_window():
    # Create the login window
    login_root = tk.Tk()
    login_root.geometry("300x150")
    login_root.title("Login")

    # Create the username label and entry field
    username_label = tk.Label(login_root, text="Username")
    username_label.pack()
    username_entry = tk.Entry(login_root)
    username_entry.pack()

    # Create the password label and entry field
    password_label = tk.Label(login_root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(login_root, show="*")
    password_entry.pack()

    # Create the login button
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the username and password are in the database
        cursor = conn.execute("SELECT * from users WHERE username = ? AND password = ?", (username, password))
        if len(cursor.fetchall()) == 1:
            # User is logged in
            login_label.config(text="Login successful!")
        else:
            # User needs to register
            login_label.config(text="Please register.")

    login_button = tk.Button(login_root, text="Login", command=login)
    login_button.pack()

    # Create the login label
    login_label = tk.Label(login_root, text="")
    login_label.pack()

    # Create the register button
    register_button = tk.Button(login_root, text="Register", command=register_window)
    register_button.pack()

    # Run the login window
    login_root.mainloop()

# Create the registration window
def register_window():
    # Create the registration window
    register_root = tk.Tk()
    register_root.geometry("300x150")
    register_root.title("Registration")

    # Create the username label and entry field
    username_label = tk.Label(register_root, text="Username")
    username_label.pack()
    username_entry = tk.Entry(register_root)
    username_entry.pack()

    # Create the password label and entry field
    password_label = tk.Label(register_root, text="Password")
    password_label.pack()
    password_entry = tk.Entry(register_root, show="*")
    password_entry.pack()

    # Create the register button
    def register():
        username = username_entry.get()
        password = password_entry.get()

        # Insert the username and password into the database
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            register_label.config(text="Registration successful!")
        except sqlite3.IntegrityError:
            register_label.config(text="Username already exists.")

    register_button = tk.Button(register_root, text="Register", command=register)
    register_button.pack()

    # Create the register label
    register_label = tk.Label(register_root, text="")
    register_label.pack()

    # Run the registration window
    register_root.mainloop()

# Run the login window
login_window()

# Close the connection to the database
conn.close()
