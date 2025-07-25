from tkinter import *
from tkinter import ttk, messagebox

# Main window
root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# Login Frame
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# Function to clear entry default text
def on_enter(e):
    user = user_entry.get()
    if user == "Username":
        user_entry.delete(0, "end")

def on_leave(e):
    name = user_entry.get()
    if name == "":
        user_entry.insert(0, "Username")

def on_enter_pass(e):
    password = pass_entry.get()
    if password == "Password":
        pass_entry.delete(0, "end")
        pass_entry.config(show="*")

def on_leave_pass(e):
    password = pass_entry.get()
    if password == "":
        pass_entry.insert(0, "Password")
        pass_entry.config(show="")

# Username Entry
user_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user_entry.place(x=30, y=80)
user_entry.insert(0, "Username")
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Password Entry
pass_entry = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
pass_entry.place(x=30, y=150)
pass_entry.insert(0, "Password")
pass_entry.bind("<FocusIn>", on_enter_pass)
pass_entry.bind("<FocusOut>", on_leave_pass)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Forgot Password
Button(frame, width=6, pady=7, text="Forgot?", bg="white", fg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 9)).place(x=250, y=200)

# Sign in Button
Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, font=("Microsoft YaHei UI Light", 10)).place(x=35, y=230)

# Sign up Prompt
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=280)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", font=("Microsoft YaHei UI Light", 9))
sign_up.place(x=215, y=280)

root.mainloop()
