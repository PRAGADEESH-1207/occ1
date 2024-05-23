import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk

# Sample list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Generate a random ID number
def generate_id():
    return ''.join(random.choices(string.digits, k=6))

# Generate a random name
def generate_name():
    return random.choice(names)

# Update the ID card with random values
def generate_card():
    random_name = generate_name()
    random_id = generate_id()
    
    name_var.set(random_name)
    id_var.set(random_id)
    
    # Display a random image
    img_path = f'images/{random.randint(1, 5)}.png'
    img = Image.open(img_path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# Initialize the main window
root = tk.Tk()
root.title("ID Card Generator")

# Variables to store name and ID
name_var = tk.StringVar()
id_var = tk.StringVar()

# Create and place the labels and entry widgets
ttk.Label(root, text="Name:").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(root, textvariable=name_var).grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="ID:").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(root, textvariable=id_var).grid(column=1, row=1, padx=10, pady=10)

# Placeholder for the image
img_label = ttk.Label(root)
img_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Button to generate a new ID card
generate_button = ttk.Button(root, text="Generate ID Card", command=generate_card)
generate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
