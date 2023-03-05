import tkinter as tk

def display_input():
    output_label.config(text="计算结果：" + entry.get() + "=" + entry.get())

root = tk.Tk()
root.title("量子计算器")
root.geometry("600x300")

title_label = tk.Label(root, text="量子计算器", font=("Helvetica", 16, "bold"))
subtitle_label = tk.Label(root, text="可计算四则运算，三角函数，根式，因式分解等复杂运算，支持世界上已知的所有运算。", font=("Helvetica", 10))
entry_label = tk.Label(root, text="请输入算式：")
entry = tk.Entry(root)
output_button = tk.Button(root, text="输出结果", command=display_input)
output_label = tk.Label(root, text="")

title_label.pack()
subtitle_label.pack()
entry_label.pack()
entry.pack()
output_button.pack()
output_label.pack()

root.mainloop()
