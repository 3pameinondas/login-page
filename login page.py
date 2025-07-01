import tkinter as tk
from tkinter import messagebox

# Define the main application window
app = tk.Tk()
app.title("Login System")
app.geometry("300x200")

# Predefined credentials
correct_username = "user"
correct_password = "pass123"

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        open_main_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

# Function to open the main screen after login
def open_main_screen():
    # Hide the login screen
    app.withdraw()
    
    # Create a new window for the main screen
    main_screen = tk.Toplevel(app)
    main_screen.title("Main Screen")
    main_screen.geometry("300x200")
    
    welcome_label = tk.Label(main_screen, text=f"Welcome, {correct_username}!", font=("Helvetica", 14))
    welcome_label.pack(pady=50)
    
    # Exit button to close the app
    exit_button = tk.Button(main_screen, text="Exit", command=app.quit)
    exit_button.pack()

# Username label and entry
username_label = tk.Label(app, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(app)
username_entry.pack()

# Password label and entry
password_label = tk.Label(app, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(app, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(app, text="Login", command=login)
login_button.pack(pady=20)

# Start the application
app.mainloop()
