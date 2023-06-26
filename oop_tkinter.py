import tkinter as tk

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GUI 1')
        tk.Label(self, text='Hello, World!').pack()


class TextFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        tk.Label(self, text='Hello, World!').pack()
        self.pack()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GUI ku')


class UsernameFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.username = tk.StringVar()
        
        self.pack()
        username_label = tk.Label(self, text='Username: ')
        username_label.pack(side='left')
        username_entry = tk.Entry(self, textvariable=self.username)
        username_entry.pack(side='left')


class ButtonFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.pack()
        greet_button = tk.Button(self, text='Greet', command=self.greet)
        greet_button.pack()
        quit_button = tk.Button(self, text='Quit', command=container.destroy)
        quit_button.pack()

    def greet(self):
        print(f"Hello, {UsernameFrame.username.get() or 'World'}!")


root = MainWindow()

UsernameFrame(root)


root.mainloop()