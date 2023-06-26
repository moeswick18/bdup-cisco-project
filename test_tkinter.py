import tkinter as tk

def greet():
    print(f"Hello, {name.get() or 'World'}!")


# tk._test()
root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.title("Greeting App")
# root.geometry("800x600")

frame_entry = tk.Frame(root)
frame_entry.grid(row=0, column=0)

label = tk.Label(
    frame_entry,
    text="Name: "
)
name = tk.StringVar()

entry = tk.Entry(
    frame_entry,
    textvariable=name
)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.rowconfigure(0, weight=1)
button_frame.grid(row=1, column=0, sticky='SNEW')

button = tk.Button(
    button_frame,
    text="Greet",
    command=greet
)

quit_button = tk.Button(
    button_frame,
    text="Quit",
    command=root.destroy
)

'''label.pack(side='left')
entry.pack(side="left", fill='x', expand=True)
button.pack(side="left", fill='both', expand=True)
quit_button.pack(side="left", fill='both', expand=True)'''
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=0, sticky='SNEW')
quit_button.grid(row=0, column=1, sticky='SNEW')

root.mainloop()

'''root = tk.Tk()
frame = tk.Frame(root)

frame.pack(side='left', fill='both', expand=True)

rectangle_1 = tk.Label(frame, text='Rectangle 1', bg='green', fg='white')
rectangle_2 = tk.Label(frame, text='Rectangle 2', bg='red', fg='white')
rectangle_3 = tk.Label(root, text='Rectangle 3', bg='blue', fg='white')

rectangle_1.pack(side='top', ipadx=10, ipady=10, fill='both', expand=True)
rectangle_2.pack(side='top', ipadx=10, ipady=10, fill='both', expand=True)
rectangle_3.pack(side='left', ipadx=10, ipady=10, fill='both', expand=True)

root.mainloop()'''
