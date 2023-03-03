import tkinter as tk
from tkinter import ttk
import time

class GeoLocationDetector:
    def __init__(self, master):
        self.master = master
        master.title("地理位置检测器")
        
        self.title_label = tk.Label(master, text="用于检测您当前的位置，防止您在茫茫宇宙中失联。")
        self.title_label.pack()
        
        self.progress_label = tk.Label(master, text="检测进程")
        self.progress_label.pack()
        
        self.progressbar = tk.ttk.Progressbar(master, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progressbar.pack()
        
        self.start_button = tk.Button(master, text="开始检测", command=self.start_detection)
        self.start_button.pack()
        
    def start_detection(self):
        self.start_button.config(state=tk.DISABLED)
        for i in range(6):
            self.progressbar["value"] = i * 20
            self.master.update()
            time.sleep(1)
        self.progress_label.config(text="检测完成，您的位置位于：拉尼亚凯亚超星系团-室女座星系团-本星系群-银河系-户臂-古尔德带-本地泡-本星际云-奥尔特云-太阳系的第三行星：地球")
        self.start_button.config(text="重新开始", state=tk.NORMAL)
        
root = tk.Tk()
geolocation_detector = GeoLocationDetector(root)
root.mainloop()
