import tkinter as tk
 
window = tk.Tk()
 
entry = tk.Entry(width=40, bg="white", fg="black")
button = tk.Button()

button.pack()
entry.pack()
 
entry.insert(0, "What is your name?")
 
window.mainloop()

