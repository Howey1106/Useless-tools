import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import random

def detect_life_signs():
    progress_bar["maximum"] = 100
    for i in range(101):
        progress_bar["value"] = i
        progress_bar.update()
        time.sleep(random.uniform(0.05, 0.1))
    messagebox.showinfo("检测结果", "用户生命体征完整，无需联系火葬场")

root = tk.Tk()
root.title("生命体征检测程序")
root.geometry("500x300")  

title_label = tk.Label(root, text="检测用户是否有生命体征", font=("Arial", 25))
title_label.pack(pady=10)

subtitle_label1 = tk.Label(root, text="可供检测您是否死亡，从而帮助您以最快的速度联系火葬场", font=("Arial", 12)) 
subtitle_label1.pack()

subtitle_label2 = tk.Label(root, text="检测时，请保持端坐，情绪稳定，深呼吸", font=("Arial", 12))
subtitle_label2.pack(pady=5)

progress_label = tk.Label(root, text="检测进度：", font=("Arial", 10)) 
progress_label.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

start_button = tk.Button(root, text="开始检测", command=detect_life_signs)
start_button.pack(pady=10)

root.mainloop()
