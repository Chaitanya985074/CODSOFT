import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_digits, use_letters, use_special_chars):
    chars = ''
    if use_digits:
        chars += string.digits
    if use_letters:
        chars += string.ascii_letters
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def copy_to_clipboard(password):
    root = tk.Tk()
    root.withdraw()
    root.update()
    root.destroy()

length = int(input("Enter the length of the password: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, use_digits, use_letters, use_special_chars)
print(f"Generated Password: {password}")

copy_to_clipboard(password)
