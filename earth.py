import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("检测地球是否毁灭")
        self.master.geometry("400x200")

        self.label = tk.Label(self.master, text="检测地球是否毁灭", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.progress = tk.IntVar()
        self.progress.set(0)
        self.progressbar = tk.ttk.Progressbar(self.master, variable=self.progress, maximum=100, length=200)
        self.progressbar.pack(pady=10)

        self.button = tk.Button(self.master, text="开始检测", command=self.check_earth)
        self.button.pack(pady=10)

    def check_earth(self):
        self.button.config(state="disabled")

        for i in range(100):
            self.progress.set(i)
            self.progressbar["value"] = i
            self.master.update()

            if random.random() < 0.2:
                self.progress.set(i + random.randint(1, 1919810))
                self.progressbar["value"] = i + random.randint(1, 1919810)
                self.master.update()

        messagebox.showinfo("检测成功", "地球没有毁灭")

        self.button.config(state="normal")
        self.progress.set(0)
        self.progressbar["value"] = 0

root = tk.Tk()
app = App(root)
root.mainloop()
