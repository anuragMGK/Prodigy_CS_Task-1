import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    # Initialize the score
    score = 0
    
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Increase score based on criteria
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    
    # Provide feedback based on the score
    if score == 5:
        feedback = "Very Strong"
    elif score == 4:
        feedback = "Strong"
    elif score == 3:
        feedback = "Moderate"
    elif score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"
    
    return feedback

def check_password_strength():
    password = password_entry.get()
    strength = password_strength(password)
    messagebox.showinfo("Password Strength", f"Password strength: {strength}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")  # Set the window size

# Define color scheme
bg_color = "#f0f0f0"
fg_color = "#333333"
btn_color = "#4CAF50"
btn_text_color = "#ffffff"
entry_bg_color = "#ffffff"
entry_fg_color = "#333333"

# Set the background color
root.configure(bg=bg_color)

# Create and place the widgets
tk.Label(root, text="Enter a password to assess its strength:", bg=bg_color, fg=fg_color, font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12), bg=entry_bg_color, fg=entry_fg_color)
password_entry.pack(pady=10)
tk.Button(root, text="Check Strength", command=check_password_strength, bg=btn_color, fg=btn_text_color, font=("Arial", 12)).pack(pady=10)

# Run the application
root.mainloop()