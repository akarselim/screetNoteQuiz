import tkinter as tk
from tkinter import PhotoImage, XView, YView

# Create window
window = tk.Tk()
window.config(padx = 20, pady = 40)
window.geometry("400x800")


def save_encrypt_fun():
    pass

def decrypt_fun():
    pass


# Create ui
    # Load the image
image_topsecret = PhotoImage(file = "topsecret.png")
image_label = tk.Label(window, image = image_topsecret)
image_label.pack()

    # Create a label for title, and make a entry for enter to title
title_label = tk.Label(window, text = "Enter your title")
title_label.pack()
title_entry = tk.Entry(window, width = 20)
title_entry.pack()

    # Create a label for secret note and make a entry for long message with text
secretnote_label = tk.Label(window, text = "Enter your secret note")
secretnote_label.pack()
secretnote_text = tk.Text()
secretnote_text.pack()

    # Create a entry for master key with entry
masterkey_label = tk.Label(window, text = "Enter master key")
masterkey_label.pack()
masterkey_entry = tk.Entry(window, width = 20)
masterkey_entry.pack()

    # Create a Save&Encryp button
save_encrypt_button = tk.Button(window, text = "Save & Encrypt", command = save_encrypt_fun)
save_encrypt_button.pack()
    # Create a Decrypte button
decrypt_button = tk.Button(window, text = "Decrypt", command = decrypt_fun)
decrypt_button.pack()


window.mainloop()