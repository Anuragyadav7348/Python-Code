import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")

root = tk.Tk()
root.title("Login Form")

tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Password").grid(row=1)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, columnspan=2)

root.mainloop()
