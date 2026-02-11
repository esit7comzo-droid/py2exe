import tkinter as tk
from tkinter import messagebox
import os

# Tkinter 루트 생성 (창 숨기기)
root = tk.Tk()
root.withdraw()  # 메인 창 숨기기

# 메시지 박스
messagebox.showinfo("알림", "hello")

# Ok 누르면 재부팅
os.system("shutdown /r /t 0")
