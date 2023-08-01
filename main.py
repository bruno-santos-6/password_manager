from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
password_locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_locker_img)
canvas.grid(column=1, row=1)

window.mainloop()