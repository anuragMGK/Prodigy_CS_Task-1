import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_value.get())
        encrypted_text = caesar_cipher(text, shift, mode='encrypt')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_value.get())
        decrypted_text = caesar_cipher(text, shift, mode='decrypt')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x400")  # Set a fixed size for the window
root.configure(bg="#f0f0f0")  # Set the background color

# Create and place input text box
input_label = tk.Label(root, text="Input Text:", bg="#f0f0f0", fg="#000")
input_label.pack(pady=(10, 0))
input_text = tk.Text(root, height=5, width=40, bg="#fff", fg="#000", bd=2)
input_text.pack(pady=(0, 10))

# Create and place shift value entry
shift_label = tk.Label(root, text="Shift Value:", bg="#f0f0f0", fg="#000")
shift_label.pack()
shift_value = tk.Entry(root, bg="#fff", fg="#000", bd=2)
shift_value.pack(pady=(0, 10))

# Create and place encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text, bg="#4CAF50", fg="#fff", bd=2, relief="raised")
encrypt_button.pack(pady=(0, 5))

# Create and place decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text, bg="#f44336", fg="#fff", bd=2, relief="raised")
decrypt_button.pack(pady=(0, 10))

# Create and place output text box
output_label = tk.Label(root, text="Output Text:", bg="#f0f0f0", fg="#000")
output_label.pack(pady=(10, 0))
output_text = tk.Text(root, height=5, width=40, bg="#fff", fg="#000", bd=2)
output_text.pack(pady=(0, 10))

# Start the GUI event loop
root.mainloop()
